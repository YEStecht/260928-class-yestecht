import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Streamlit 요소 탐험실",
    page_icon=":material/widgets:",
    layout="wide",
)


@st.cache_data
def get_sample_data():
    """Create a small, self-contained dataset for the component examples."""
    data = pd.DataFrame(
        [
            {"작업": "랜딩 페이지 개선", "팀": "디자인", "상태": "진행 중", "우선순위": "높음", "진척도": 72, "마감일": "2026-10-02", "위도": 37.5665, "경도": 126.9780},
            {"작업": "API 문서 정리", "팀": "플랫폼", "상태": "완료", "우선순위": "보통", "진척도": 100, "마감일": "2026-09-24", "위도": 35.1796, "경도": 129.0756},
            {"작업": "모바일 QA", "팀": "품질", "상태": "진행 중", "우선순위": "높음", "진척도": 48, "마감일": "2026-10-06", "위도": 37.4563, "경도": 126.7052},
            {"작업": "월간 회고", "팀": "운영", "상태": "대기", "우선순위": "낮음", "진척도": 10, "마감일": "2026-10-09", "위도": 36.3504, "경도": 127.3845},
            {"작업": "검색 기능 시안", "팀": "디자인", "상태": "완료", "우선순위": "보통", "진척도": 100, "마감일": "2026-09-29", "위도": 35.8714, "경도": 128.6014},
            {"작업": "접근성 점검", "팀": "품질", "상태": "대기", "우선순위": "높음", "진척도": 0, "마감일": "2026-10-12", "위도": 33.4996, "경도": 126.5312},
            {"작업": "배포 자동화", "팀": "플랫폼", "상태": "진행 중", "우선순위": "높음", "진척도": 64, "마감일": "2026-10-04", "위도": 36.6424, "경도": 127.4890},
            {"작업": "사용자 인터뷰", "팀": "운영", "상태": "완료", "우선순위": "보통", "진척도": 100, "마감일": "2026-09-26", "위도": 35.1595, "경도": 126.8526},
        ]
    )
    data["마감일"] = pd.to_datetime(data["마감일"])
    return data


sample_data = get_sample_data()

with st.sidebar:
    st.title(":material/tune: 보기 설정")
    st.caption("앱에 포함된 샘플 작업 데이터를 사용합니다")
    st.divider()
    selected_teams = st.multiselect(
        "팀 필터",
        options=sample_data["팀"].unique().tolist(),
        default=sample_data["팀"].unique().tolist(),
    )
    selected_statuses = st.multiselect(
        "상태 필터",
        options=["진행 중", "대기", "완료"],
        default=["진행 중", "대기", "완료"],
    )
    minimum_progress = st.slider("최소 진척도", 0, 100, 0, step=10, format="%d%%")
    show_map = st.toggle("지도 표시", value=True)

filtered_data = sample_data[
    sample_data["팀"].isin(selected_teams)
    & sample_data["상태"].isin(selected_statuses)
    & (sample_data["진척도"] >= minimum_progress)
].copy()

st.title(":material/widgets: Streamlit 요소 탐험실")
st.markdown("차트, 데이터 표시, 입력 위젯, 레이아웃과 알림을 한 페이지에서 살펴보세요.")
st.caption("모든 화면은 앱에 포함된 샘플 프로젝트 데이터로 동작합니다.")
st.divider()

overview_tab, data_tab, widgets_tab, display_tab = st.tabs(
    ["현황", "데이터", "입력 위젯", "표현 요소"]
)

with overview_tab:
    st.header("프로젝트 현황", divider="gray")
    metric_columns = st.columns(4)
    total_tasks = len(filtered_data)
    completed_tasks = int((filtered_data["상태"] == "완료").sum())
    average_progress = filtered_data["진척도"].mean() if total_tasks else 0
    metric_columns[0].metric("표시 작업", f"{total_tasks}", delta="필터 적용")
    metric_columns[1].metric("완료", f"{completed_tasks}", delta=f"전체 {len(sample_data)}개 중")
    metric_columns[2].metric("평균 진척도", f"{average_progress:.0f}%", delta="현재 선택 기준")
    metric_columns[3].metric("참여 팀", f"{filtered_data['팀'].nunique()}", delta="개 팀")

    chart_column, progress_column = st.columns([3, 2])
    with chart_column:
        st.subheader("팀별 작업 현황")
        if filtered_data.empty:
            st.info("조건에 맞는 작업이 없습니다.")
        else:
            team_summary = filtered_data.groupby("팀", as_index=False)["진척도"].mean()
            st.bar_chart(team_summary, x="팀", y="진척도")
    with progress_column:
        st.subheader("작업별 진척도")
        if filtered_data.empty:
            st.info("표시할 진척도가 없습니다.")
        else:
            progress_data = filtered_data[["작업", "진척도"]].set_index("작업")
            st.area_chart(progress_data)

    if show_map:
        st.subheader("팀 위치")
        if filtered_data.empty:
            st.info("지도에 표시할 작업이 없습니다.")
        else:
            st.map(filtered_data.rename(columns={"위도": "latitude", "경도": "longitude"}))

    with st.expander("현황 요약 보기"):
        st.write(f"선택한 조건의 작업은 **{total_tasks}개**이며 평균 진척도는 **{average_progress:.0f}%**입니다.")

with data_tab:
    st.header("데이터 표시와 다운로드", divider="gray")
    st.write(f"필터 결과 **{len(filtered_data)}행**")
    edited_data = st.data_editor(
        filtered_data.drop(columns=["위도", "경도"]),
        width="stretch",
        hide_index=True,
        num_rows="dynamic",
        column_config={
            "진척도": st.column_config.ProgressColumn("진척도", min_value=0, max_value=100, format="%d%%"),
            "마감일": st.column_config.DateColumn("마감일", format="YYYY-MM-DD"),
            "상태": st.column_config.SelectboxColumn("상태", options=["대기", "진행 중", "완료"]),
        },
    )
    st.download_button(
        "현재 표 CSV 다운로드",
        data=edited_data.to_csv(index=False).encode("utf-8-sig"),
        file_name="sample_tasks.csv",
        mime="text/csv",
        icon=":material/download:",
    )
    with st.expander("기본 표와 요약 통계"):
        st.table(filtered_data[["작업", "팀", "상태", "진척도"]].head(5))
        if not filtered_data.empty:
            st.json({"작업 수": total_tasks, "완료 수": completed_tasks, "팀": sorted(filtered_data["팀"].unique())})

with widgets_tab:
    st.header("입력 위젯 모음", divider="gray")
    st.write("각 입력을 바꾸면 선택한 값이 앱에 반영됩니다.")
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("선택과 값 입력")
        st.segmented_control("화면 모드", ["요약", "상세", "비교"], default="요약", key="demo_segment")
        st.selectbox("담당 팀", sample_data["팀"].unique(), key="demo_selectbox")
        st.radio("정렬 순서", ["마감일순", "진척도순", "우선순위순"], horizontal=True, key="demo_radio")
        st.select_slider("만족도", ["낮음", "보통", "높음", "매우 높음"], value="높음", key="demo_select_slider")
        st.number_input("목표 작업 수", min_value=1, max_value=100, value=12, key="demo_number")
        st.color_picker("강조 색상", value="#168C86", key="demo_color")

    with right_column:
        st.subheader("텍스트와 일정")
        st.text_input("검색어", placeholder="작업 이름", key="demo_text")
        st.text_area("메모", placeholder="간단한 메모를 입력하세요", key="demo_text_area")
        st.date_input("기준 날짜", key="demo_date")
        st.time_input("알림 시각", key="demo_time")
        st.slider("강조 진척도", 0, 100, 60, key="demo_slider")
        st.checkbox("완료 항목 포함", value=True, key="demo_checkbox")
        st.toggle("알림 사용", value=False, key="demo_toggle")

    st.file_uploader("CSV 파일 선택", type=["csv"], key="demo_file")
    st.camera_input("사진 촬영 또는 업로드", key="demo_camera")

    with st.form("demo_form", border=True):
        st.subheader("폼 입력 후 한 번에 제출")
        form_title = st.text_input("요청 제목", value="새 작업 요청", key="form_title")
        form_priority = st.selectbox("우선순위", ["낮음", "보통", "높음"], key="form_priority")
        st.text_area("요청 내용", key="form_details")
        form_submitted = st.form_submit_button("요청 등록", type="primary", icon=":material/check:")
    if form_submitted:
        st.success(f"'{form_title}' 요청을 등록했습니다. 우선순위: {form_priority}")

    action_column, popup_column = st.columns(2)
    with action_column:
        if st.button("토스트 알림 표시", icon=":material/notifications:"):
            st.toast("작업이 완료되었습니다", icon=":material/check_circle:")
    with popup_column:
        with st.popover("추가 옵션", icon=":material/settings:"):
            st.write("팝오버 안의 콘텐츠")
            st.toggle("간결한 보기", key="demo_compact")

with display_tab:
    st.header("텍스트와 상태 표시", divider="gray")
    st.markdown("**Markdown** · 제목, 목록, 링크와 서식을 넣을 수 있습니다.")
    st.markdown("- 안내와 도움말\n- [Streamlit 문서](https://docs.streamlit.io/)")
    st.caption("caption으로 출처나 짧은 보조 설명을 표시합니다.")
    st.divider()

    message_column, status_column = st.columns(2)
    with message_column:
        st.success("성공 메시지")
        st.info("정보 안내")
        st.warning("주의 메시지")
        st.error("오류 메시지 예시")
    with status_column:
        st.progress(68, text="작업 진행률")
        with st.status("작업 상태 확인", expanded=True) as status:
            st.write("입력 확인 중")
            st.write("결과 준비 완료")
            status.update(label="완료", state="complete", expanded=False)
        if st.button("로딩 표시 체험", key="spinner_button"):
            with st.spinner("처리 중..."):
                st.write("처리가 끝났습니다.")

    st.subheader("코드, JSON, 수식")
    code_column, json_column = st.columns(2)
    with code_column:
        st.code("st.metric('완료 작업', 8, delta='2개 증가')", language="python")
    with json_column:
        st.json({"project": "sample", "tasks": len(filtered_data), "teams": sorted(filtered_data["팀"].unique())})
    st.latex(r"진척률 = \frac{완료한\ 작업}{전체\ 작업} \times 100")

    with st.container(border=True):
        st.subheader("컨테이너 안의 콘텐츠")
        st.write("컨테이너는 관련된 요소를 한 영역에 묶을 때 사용합니다.")
        st.feedback("thumbs", key="demo_feedback")

    if st.button("임시 영역 비우기"):
        st.empty()
