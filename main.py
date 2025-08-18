import streamlit as st

# MBTI별 추천 직업 목록 (시윤님의 ISFP도 포함했어요! 🎨)
mbti_recommendations = {
    "ISTJ": ["회계사", "공무원", "경찰관", "데이터 분석가"],
    "ISFJ": ["간호사", "사회복지사", "교사", "사서"],
    "INFJ": ["상담사", "작가", "심리학자", "인사 담당자"],
    "INTJ": ["과학자", "엔지니어", "교수", "전략 컨설턴트"],
    "ISTP": ["개발자", "기술자", "경찰관", "소방관"],
    "ISFP": ["예술가", "디자이너", "요리사", "수의사 보조", "재료 공학자"], # 시윤님 ISFP를 위해 여러 직업을 넣어봤어요!
    "INFP": ["작가", "음악가", "컨설턴트", "그래픽 디자이너"],
    "INTP": ["연구원", "프로그래머", "철학자", "시스템 분석가"],
    "ESTP": ["영업사원", "사업가", "경찰관", "운동선수"],
    "ESFP": ["연예인", "이벤트 플래너", "유치원 교사", "서비스업 종사자"],
    "ENFP": ["크리에이터", "컨설턴트", "강사", "광고 기획자"],
    "ENTP": ["창업가", "변호사", "발명가", "프리랜서 개발자"],
    "ESTJ": ["경영자", "변호사", "군인", "관리자"],
    "ESFJ": ["교사", "영업사원", "사회복지사", "고객 서비스 담당자"],
    "ENFJ": ["리더", "정치가", "상담사", "비영리 단체 활동가"],
    "ENTJ": ["기업가", "변호사", "경영 컨설턴트", "프로젝트 관리자"],
}

st.set_page_config(
    page_title="MBTI별 직업 추천 앱",
    page_icon="✨",
    layout="centered"
)

# 웹 앱 제목 설정
st.title("MBTI별 맞춤 직업 추천 웹 앱 ✨")
st.write("---")

st.markdown("""
당신의 MBTI 유형은 무엇인가요? 🕵️‍♀️

궁금한 MBTI를 선택하고, 숨겨진 직업의 세계를 탐험해 보세요!
""")

# MBTI 유형 선택 드롭다운 메뉴
mbti_types = list(mbti_recommendations.keys())
selected_mbti = st.selectbox(
    "당신의 MBTI 유형을 선택해 주세요:",
    options=mbti_types,
    index=mbti_types.index("ISFP") if "ISFP" in mbti_types else 0, # 기본값을 시윤님의 MBTI로 설정해봤어요!
    help="본인의 MBTI를 선택하시면 해당 유형에 맞는 직업을 추천해 드립니다."
)

st.write(f"") # 간격 조절

# "직업 추천받기!" 버튼
if st.button("직업 추천받기! 🌟"):
    st.subheader(f"✨ **{selected_mbti}** 유형에게 추천하는 직업은요...")
    
    # 선택된 MBTI에 대한 직업 추천 가져오기
    jobs = mbti_recommendations.get(selected_mbti, [])

    if jobs:
        for job in jobs:
            st.success(f"✔️ {job}")
        st.info("이 추천은 일반적인 경향이며, 개인의 역량과 관심사에 따라 다양하게 해석될 수 있습니다! 😉")
    else:
        st.warning("아직 이 MBTI 유형에 대한 직업 정보가 준비되지 않았어요. ㅠㅠ")

st.write("---")
st.markdown("""
<div style="text-align: center;">
    <p>💡 이 앱은 <a href="https://streamlit.io/" target="_blank">Streamlit</a>으로 만들어졌습니다! 🚀</p>
    <p>더 다양한 기능을 추가하며 자신만의 앱을 만들어 보세요! </p>
</div>
""", unsafe_allow_html=True)

