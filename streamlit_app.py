from datetime import date

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="양은선 | 기술 교사",
    page_icon=":material/school:",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: var(--background-color);
        background-image: radial-gradient(color-mix(in srgb, var(--primary-color) 10%, transparent) 0.7px, transparent 0.7px);
        background-size: 22px 22px;
    }
    .block-container {
        max-width: 1080px;
        padding-top: 2.8rem;
        padding-bottom: 4rem;
    }
    h1, h2, h3, p, button, label {
        font-family: 'Noto Sans KR', sans-serif;
        letter-spacing: 0;
    }
    h1 {
        font-family: 'Gowun Batang', serif;
        font-size: 3.7rem !important;
        color: var(--text-color);
        line-height: 1.2 !important;
        animation: arrive 650ms ease-out both;
    }
    h2, h3 { color: var(--text-color); }
    .intro-kicker {
        color: var(--primary-color);
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        animation: arrive 450ms ease-out both;
    }
    .intro-copy {
        color: var(--text-color);
        font-size: 1.15rem;
        line-height: 1.9;
        max-width: 720px;
        animation: arrive 800ms ease-out both;
    }
    .fact-label {
        color: var(--primary-color);
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .fact-value {
        color: var(--text-color);
        font-family: 'Gowun Batang', serif;
        font-size: 1.4rem;
        font-weight: 700;
    }
    [data-testid='stImage'] img { border-radius: 4px; }
    div.stButton > button, div.stPageLink > a {
        border-radius: 4px;
        min-height: 2.7rem;
        font-weight: 600;
    }
    @keyframes arrive {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @media (max-width: 640px) {
        .block-container { padding-top: 1.8rem; }
        h1 { font-size: 2.8rem !important; }
        .intro-copy { font-size: 1.02rem; }
    }
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

for counter_key in ("cheer_balloons", "cheer_parent_mode", "cheer_parenting_page"):
    st.session_state.setdefault(counter_key, 0)


def render_home():
    st.markdown('<div class="intro-kicker">기술 교사 · 불광중학교</div>', unsafe_allow_html=True)
    st.title("양은선")
    st.markdown(
        '<p class="intro-copy">교실에서는 기술을 함께 배우고, 집에서는 돌쟁이 아기와 함께 하루하루 자라는 중입니다.<br>'
        '학교와 육아, 두 세계의 이야기를 나눠요.</p>',
        unsafe_allow_html=True,
    )

    cheer_col, parent_col, _ = st.columns([1.2, 1.35, 4.5])
    with cheer_col:
        if st.button("응원 풍선 보내기", icon=":material/celebration:", width="stretch"):
            st.session_state["cheer_balloons"] += 1
            st.balloons()
            st.toast("양은선 선생님에게 응원을 보냈어요!", icon=":material/favorite:")
        st.metric("풍선 응원", f"{st.session_state['cheer_balloons']}회", help="현재 접속 세션 기준")
    with parent_col:
        if st.button("육아 모드 응원하기", icon=":material/child_care:", width="stretch"):
            st.session_state["cheer_parent_mode"] += 1
            st.snow()
            st.toast("오늘도 멋지게 해내는 중!", icon=":material/star:")
        st.metric("육아 모드 응원", f"{st.session_state['cheer_parent_mode']}회", help="현재 접속 세션 기준")

    st.divider()
    st.markdown("### 양은선을 소개합니다")
    fact_cols = st.columns(3, gap="large")
    facts = [("담당 과목", "기술"), ("근무 학교", "불광중학교"), ("요즘의 나", "돌쟁이 아기와 성장 중")]
    for column, (label, value) in zip(fact_cols, facts):
        with column:
            st.markdown(
                f'<div class="fact-label">{label}</div><div class="fact-value">{value}</div>',
                unsafe_allow_html=True,
            )

    st.divider()
    photo_col, story_col = st.columns([1, 1], gap="large", vertical_alignment="center")
    with photo_col:
        st.image(
            "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1200&q=85",
            caption="수업의 영감이 되는 교실 풍경 (참고 이미지)",
            width="stretch",
        )
    with story_col:
        st.subheader("교실에서, 집에서")
        st.write(
            "기술 시간에는 아이디어를 손으로 만들어 보는 즐거움을 나누고, "
            "집에서는 돌쟁이 아기와 처음 만나는 것들을 함께 배우고 있어요. "
            "서로 다른 두 공간에서 매일 조금씩 성장하는 중입니다."
        )
        st.page_link(technology_page, label="기술 교과 페이지", icon=":material/precision_manufacturing:")
        st.page_link(parenting_page, label="육아 이야기 페이지", icon=":material/child_care:")
    st.divider()
    st.caption("오늘도 교실과 집에서, 작은 발견을 모으는 중입니다.")


def render_technology():
    st.markdown('<div class="intro-kicker">CLASSROOM / TECHNOLOGY</div>', unsafe_allow_html=True)
    st.title("기술 교과")
    st.markdown("생활 속 문제를 발견하고, 아이디어를 설계하고, 직접 만들어 보는 수업 아이디어를 탐색합니다.")
    st.info("아래 내용은 수업 구성을 살펴보기 위한 예시입니다. 실제 학교 수업 계획을 나타내지는 않습니다.", icon=":material/lightbulb:")

    idea_tab, planner_tab, quiz_tab = st.tabs(["수업 아이디어", "수업 설계 실험실", "기술 퀴즈"])

    with idea_tab:
        topic = st.selectbox(
            "탐색할 주제",
            ["생활 속 문제 해결", "재료와 구조", "지속 가능한 기술", "디지털 생활"],
        )
        ideas = {
            "생활 속 문제 해결": "학교나 집에서 불편한 점을 찾아보고, 사용자의 입장에서 해결 아이디어를 제안합니다.",
            "재료와 구조": "종이·나무·재활용 재료의 특성을 비교하고, 튼튼하고 쓰기 편한 구조를 구상합니다.",
            "지속 가능한 기술": "물건의 생산부터 폐기까지 살펴보고, 자원을 덜 쓰는 개선 방법을 찾아봅니다.",
            "디지털 생활": "일상에서 쓰는 디지털 기술의 편리함과 책임 있는 사용 방법을 함께 생각합니다.",
        }
        st.subheader(topic)
        st.write(ideas[topic])
        stage_cols = st.columns(3)
        for column, (number, stage, detail) in zip(
            stage_cols,
            [
                ("01", "발견하기", "누구의 어떤 문제인지 살펴보기"),
                ("02", "설계하기", "아이디어를 그리고 비교하기"),
                ("03", "나누기", "결과를 시험하고 개선점 이야기하기"),
            ],
        ):
            with column:
                st.markdown(f"#### {number} · {stage}")
                st.caption(detail)
        st.subheader("한 차시 흐름 예시")
        lesson_flow = pd.DataFrame(
            {
                "단계": ["문제 발견", "아이디어 스케치", "공유와 피드백"],
                "활동 비중(%)": [25, 45, 30],
            }
        )
        st.bar_chart(lesson_flow, x="단계", y="활동 비중(%)")
        with st.expander("생각을 여는 질문 예시"):
            st.markdown(
                "- 이 물건은 누구를 위해 만들어졌을까요?\n"
                "- 사용하기 불편한 순간은 언제일까요?\n"
                "- 더 안전하고 오래 쓰려면 무엇을 바꾸면 좋을까요?"
            )

    with planner_tab:
        st.write("주제와 조건을 고르면 수업 설계 초안을 만들어 봅니다.")
        with st.form("lesson_planner", border=True):
            grade = st.selectbox("대상 학년", ["1학년", "2학년", "3학년"])
            plan_topic = st.selectbox("수업 주제", ["생활 속 문제 해결", "재료와 구조", "지속 가능한 기술", "디지털 생활"])
            periods = st.number_input("수업 차시", min_value=1, max_value=12, value=2)
            focus = st.multiselect("강조할 경험", ["관찰", "아이디어 스케치", "만들기", "협력", "발표와 피드백"], default=["관찰", "만들기"])
            plan_submitted = st.form_submit_button("설계 초안 만들기", type="primary", icon=":material/auto_awesome:")
        if plan_submitted:
            st.session_state["lesson_plan"] = {
                "grade": grade,
                "topic": plan_topic,
                "periods": periods,
                "focus": focus,
            }
        if "lesson_plan" in st.session_state:
            plan = st.session_state["lesson_plan"]
            st.success(f"{plan['grade']} · {plan['topic']} · {plan['periods']}차시 초안을 만들었습니다.")
            st.progress(min(len(plan["focus"]) / 5, 1.0), text=f"선택한 학습 경험 {len(plan['focus'])}개")
            plan_table = pd.DataFrame(
                {
                    "수업 단계": ["열기", "탐색·설계", "공유·성찰"],
                    "활동 예시": ["생활 속 문제 찾기", "아이디어를 구체화하고 시험하기", "결과와 개선점 나누기"],
                    "강조 경험": [", ".join(plan["focus"]) or "자유 선택"] * 3,
                }
            )
            st.dataframe(plan_table, width="stretch", hide_index=True)
            st.download_button(
                "설계 초안 CSV 다운로드",
                data=plan_table.to_csv(index=False).encode("utf-8-sig"),
                file_name="수업_설계_초안.csv",
                mime="text/csv",
                icon=":material/download:",
            )

    with quiz_tab:
        st.subheader("종이 다리를 더 튼튼하게 만들려면?")
        with st.form("technology_quiz"):
            answer = st.radio(
                "가장 적절한 방법을 골라 보세요.",
                ["종이를 여러 번 접어 단면의 높이를 키운다", "종이를 한 장 더 평평하게 올린다", "다리의 폭을 더 좁게 만든다"],
            )
            quiz_submitted = st.form_submit_button("정답 확인", icon=":material/check:")
        if quiz_submitted:
            if answer == "종이를 여러 번 접어 단면의 높이를 키운다":
                st.success("정답이에요! 단면의 모양을 바꾸면 종이가 휘는 것을 줄일 수 있습니다.")
                st.balloons()
            else:
                st.info("힌트: 재료를 더하지 않고 단면의 모양을 바꾸는 방법을 생각해 보세요.")
        st.feedback("thumbs", key="technology_feedback")


def render_parenting():
    st.markdown('<div class="intro-kicker">LITTLE MOMENTS / PARENTING</div>', unsafe_allow_html=True)
    st.title("육아 이야기")
    st.markdown("돌쟁이 아기와 함께 보내는 하루. 작고 정신없는 순간도 나중엔 반짝이는 기억이 되니까요.")
    st.info("아래 기록은 이 화면에서만 확인하는 예시예요. 따로 저장되거나 전송되지 않습니다.", icon=":material/lock:")

    moments_col, mood_col = st.columns([1.15, 1], gap="large")
    with moments_col:
        st.subheader("오늘의 작은 순간")
        moments = st.multiselect(
            "오늘 있었던 순간을 골라 보세요",
            ["함께 웃기", "새로운 것 발견", "산책하기", "밥 먹기", "낮잠 자기", "무사히 하루 보내기"],
        )
        st.metric("오늘의 순간", f"{len(moments)}개", delta="기록 중" if moments else "천천히 골라 보세요")
        st.progress(min(len(moments) / 6, 1.0), text="오늘을 채운 순간")
    with mood_col:
        st.subheader("오늘의 기분")
        mood = st.select_slider("나의 에너지", options=["방전", "저전력", "보통", "충전 중", "풀충전"], value="보통")
        mood_messages = {
            "방전": "오늘은 버틴 것만으로도 충분해요.",
            "저전력": "작은 휴식 하나를 나에게 선물해요.",
            "보통": "무리하지 않고 나다운 속도로 가요.",
            "충전 중": "좋은 기운을 천천히 모으고 있네요.",
            "풀충전": "오늘의 에너지를 마음껏 누려요!",
        }
        st.success(mood_messages[mood], icon=":material/volunteer_activism:")

    st.divider()
    st.subheader("오늘의 한 줄 기록")
    with st.form("parenting_journal", border=True):
        entry_date = st.date_input("날짜", value=date.today())
        entry_title = st.text_input("오늘을 한마디로", placeholder="예: 작은 손으로 박수 친 날")
        entry_note = st.text_area("기억해 두고 싶은 순간", placeholder="짧게 적어도 괜찮아요.")
        journal_submitted = st.form_submit_button("오늘 기록 보기", type="primary", icon=":material/edit_note:")
    if journal_submitted:
        st.markdown(f"### {entry_date:%Y년 %-m월 %-d일} · {entry_title or '오늘도 함께 자란 날'}")
        if entry_note:
            st.write(entry_note)
        if moments:
            st.caption("오늘의 순간: " + " · ".join(moments))
        st.balloons()
        st.toast("오늘의 기록을 화면에 남겼어요", icon=":material/auto_awesome:")

    with st.expander("돌쟁이와 보내는 하루, 이런 순간도 있어요"):
        st.markdown(
            "- 처음 해보는 표정과 몸짓을 발견하기\n"
            "- 같이 웃다가 이유를 잊어버리기\n"
            "- 계획대로 되지 않아도 오늘을 무사히 보내기"
        )
    if st.button("작은 응원 받기", icon=":material/favorite:"):
        st.session_state["cheer_parenting_page"] += 1
        st.snow()
        st.toast("지금도 충분히 잘하고 있어요.", icon=":material/child_care:")
    st.metric("작은 응원 누적", f"{st.session_state['cheer_parenting_page']}회", help="현재 접속 세션 기준")
    st.feedback("thumbs", key="parenting_feedback")


home_page = st.Page(render_home, title="소개", icon=":material/person:", default=True)
technology_page = st.Page(render_technology, title="기술 교과", icon=":material/precision_manufacturing:")
parenting_page = st.Page(render_parenting, title="육아 이야기", icon=":material/child_care:")

with st.sidebar:
    st.markdown("### 양은선")
    st.caption("기술 교사 · 불광중학교")
    st.divider()

current_page = st.navigation(
    {
        "양은선의 페이지": [home_page],
        "이야기": [technology_page, parenting_page],
    },
    position="sidebar",
)
current_page.run()
