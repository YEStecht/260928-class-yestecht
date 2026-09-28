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
        background-color: #f4f7f3;
        background-image: radial-gradient(#dce7df 0.7px, transparent 0.7px);
        background-size: 22px 22px;
    }
    .block-container {
        max-width: 1080px;
        padding-top: 3.2rem;
        padding-bottom: 4rem;
    }
    h1, h2, h3, p, button, label {
        font-family: 'Noto Sans KR', sans-serif;
        letter-spacing: 0;
    }
    h1 {
        font-family: 'Gowun Batang', serif;
        font-size: 4rem !important;
        color: #173c38;
        line-height: 1.2 !important;
        animation: arrive 700ms ease-out both;
    }
    h2, h3 {
        color: #173c38;
    }
    .intro-kicker {
        color: #d2674c;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        animation: arrive 500ms ease-out both;
    }
    .intro-copy {
        color: #38514b;
        font-size: 1.18rem;
        line-height: 1.9;
        max-width: 680px;
        animation: arrive 850ms ease-out both;
    }
    .section-note {
        color: #586b65;
        font-size: 1.02rem;
        line-height: 1.9;
    }
    .fact-label {
        color: #d2674c;
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .fact-value {
        color: #173c38;
        font-family: 'Gowun Batang', serif;
        font-size: 1.45rem;
        font-weight: 700;
    }
    [data-testid='stImage'] img {
        border-radius: 4px;
        animation: arrive 900ms ease-out both;
    }
    div.stButton > button {
        border-radius: 4px;
        min-height: 2.8rem;
        font-weight: 600;
    }
    @keyframes arrive {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @media (max-width: 640px) {
        .block-container { padding-top: 2rem; }
        h1 { font-size: 3rem !important; }
        .intro-copy { font-size: 1.05rem; }
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

st.markdown('<div class="intro-kicker">기술 교사 · 불광중학교</div>', unsafe_allow_html=True)
st.title("양은선")
st.markdown(
    '<p class="intro-copy">안녕하세요. 불광중학교에서 기술을 가르치는 양은선입니다.<br>'
    '교실에서는 함께 만들고 배우고, 집에서는 돌쟁이 아기와 함께 하루하루 자라는 중입니다.</p>',
    unsafe_allow_html=True,
)

cheer_col, baby_col, _ = st.columns([1.3, 1.45, 5])
with cheer_col:
    if st.button("응원 풍선 보내기", icon=":material/celebration:", width="stretch"):
        st.balloons()
        st.toast("양은선 선생님에게 응원을 보냈어요!", icon=":material/favorite:")
with baby_col:
    if st.button("육아 모드 응원하기", icon=":material/child_care:", width="stretch"):
        st.snow()
        st.toast("오늘도 멋지게 해내는 중!", icon=":material/star:")

st.divider()

photo_col, story_col = st.columns([1.05, 1], gap="large", vertical_alignment="center")
with photo_col:
    st.image(
        "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1200&q=85",
        caption="수업의 영감이 되는 교실의 풍경",
        width="stretch",
    )
with story_col:
    st.markdown("### 교실에서, 집에서")
    st.markdown(
        '<p class="section-note">기술 시간에는 아이디어를 손으로 만들어 보는 즐거움을 나눕니다. '
        '집에서는 돌쟁이 아기와 처음 만나는 것들을 함께 배우고 있어요. '
        '서로 다른 두 공간에서 매일 조금씩 성장하는 중입니다.</p>',
        unsafe_allow_html=True,
    )

st.divider()
st.markdown("### 양은선을 소개합니다")
info_col1, info_col2, info_col3 = st.columns(3, gap="large")
with info_col1:
    st.markdown('<div class="fact-label">담당 과목</div><div class="fact-value">기술</div>', unsafe_allow_html=True)
with info_col2:
    st.markdown('<div class="fact-label">근무 학교</div><div class="fact-value">불광중학교</div>', unsafe_allow_html=True)
with info_col3:
    st.markdown('<div class="fact-label">요즘의 나</div><div class="fact-value">돌쟁이 아기와 성장 중</div>', unsafe_allow_html=True)

st.divider()
st.caption("오늘도 교실과 집에서, 작은 발견을 모으는 중입니다.")
