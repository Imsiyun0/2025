import streamlit as st

# MBTI별 추천 직업 목록 (시윤님의 ISFP는 더 빛나게! 🌟)
mbti_recommendations = {
    "ISTJ": ["회계사 📊", "공무원 🧑‍⚖️", "경찰관 👮‍♂️", "데이터 분석가 📈"],
    "ISFJ": ["간호사 👩‍⚕️", "사회복지사 🤝", "교사 👩‍🏫", "사서 📚"],
    "INFJ": ["상담사 🗣️", "작가 ✍️", "심리학자 🧠", "인사 담당자 🧑‍💼"],
    "INTJ": ["과학자 🔬", "엔지니어 👷", "교수 🎓", "전략 컨설턴트 ♟️"],
    "ISTP": ["개발자 💻", "기술자 🛠️", "경찰관 👮‍♂️", "소방관 🚒"],
    "ISFP": ["예술가 🎨✨", "디자이너 🖌️💡", "요리사 🍳🧑‍🍳", "수의사 보조 🐾❤️", "재료 공학자 🧪🔬"], # 시윤님 ISFP에 더 반짝임을!
    "INFP": ["작가 ✍️📚", "음악가 🎶🎵", "컨설턴트 💡🧠", "그래픽 디자이너 🖼️💻"],
    "INTP": ["연구원 🧑‍🔬🔭", "프로그래머 💻⌨️", "철학자 🤔✨", "시스템 분석가 🖥️📊"],
    "ESTP": ["영업사원 💼💰", "사업가 📈🚀", "경찰관 👮‍♂️🚨", "운동선수 🏅🏆"],
    "ESFP": ["연예인 🎤🤩", "이벤트 플래너 🎉🎈", "유치원 교사 🧑‍🎓👧", "서비스업 종사자 🏨😊"],
    "ENFP": ["크리에이터 🎥🎬", "컨설턴트 🗣️💡", "강사 🎤🎓", "광고 기획자 📝🌟"],
    "ENTP": ["창업가 🚀💡", "변호사 ⚖️🧑‍⚖️", "발명가 🤯✨", "프리랜서 개발자 💻🌍"],
    "ESTJ": ["경영자 👔💼", "변호사 ⚖️👨‍⚖️", "군인 🎖️💪", "관리자 📋✨"],
    "ESFJ": ["교사 👩‍🏫🍎", "영업사원 💼🤝", "사회복지사 🫂💖", "고객 서비스 담당자 📞😊"],
    "ENFJ": ["리더 👑🌟", "정치가 🏛️🗣️", "상담사 🗣️💡", "비영리 단체 활동가 🌱💖"],
    "ENTJ": ["기업가 🏢🚀", "변호사 ⚖️👨‍⚖️", "경영 컨설턴트 📈💡", "프로젝트 관리자 🗓️✔️"],
}

st.set_page_config(
    page_title="💖 반짝반짝 MBTI 직업 추천소 🔮", # 페이지 제목에도 이모지를!
    page_icon="🌈", # 브라우저 탭에 나타나는 아이콘도 무지개로!
    layout="centered", # 페이지 레이아웃 중앙 정렬
    initial_sidebar_state="collapsed" # 사이드바 초기 상태 (필요 없으면 제거)
)

# 웹 앱 제목 설정 - 정말 화려하고 예쁘게!
st.title("🌟✨ 내 MBTI는 어디로? 반짝반짝 맞춤 직업 추천소! ✨🌟")
st.write("---") # 시각적인 구분선

st.markdown("""
<div style="font-size: 1.2em; text-align: center; color: #5B487A; font-weight: bold;">
    **시윤님, 안녕하세요! 😊**<br>
    당신의 MBTI 유형은 무엇인가요? 🕵️‍♀️🔍<br>
    궁금한 MBTI를 선택하고, **숨겨진 직업의 세계를 신나게 탐험해 보세요! 🌈🚀**<br>
    당신이 꿈꾸는 미래를 함께 찾아볼까요? 💖
</div>
""", unsafe_allow_html=True)

st.write(" ") # 간격 조절

# MBTI 유형 선택 드롭다운 메뉴 - 설명도 더 예쁘게
st.markdown("👇 **당신의 매력을 발산할 MBTI 유형을 반짝이는 목록에서 선택해 주세요!** 👇")
mbti_types = list(mbti_recommendations.keys())
selected_mbti = st.selectbox(
    " ", # selectbox 레이블을 비워서 위에 마크다운으로 설명 붙이기
    options=mbti_types,
    index=mbti_types.index("ISFP") if "ISFP" in mbti_types else 0, # 시윤님 MBTI가 기본으로! ㅎㅎ
    help="본인의 MBTI를 선택하시면 해당 유형에 맞는 직업을 추천해 드립니다. 💫"
)

st.write(" ") # 간격 조절

# "직업 추천받기!" 버튼 - 클릭하면 신나는 효과가!
if st.button("✨💖 나만의 맞춤 직업 찾기! 🚀💖✨"):
    st.write("---") # 시각적 구분선 추가
    st.subheader(f"🎉 **{selected_mbti}** 유형에게 빛나는 추천 직업은요... 🤩")
    
    jobs = mbti_recommendations.get(selected_mbti, [])

    if jobs:
        # 직업 목록을 예쁜 이모지와 함께 출력
        for job in jobs:
            st.success(f"✔️ **{job}**") # 각 직업에도 반짝이는 이모지 추가!
        st.info("💡 이 추천은 일반적인 경향이며, 시윤님의 개성과 역량, 그리고 열정으로 얼마든지 멋지게 바꿔나갈 수 있다는 거 잊지 마세요! 😉✨")
        st.balloons() # 와! 풍선이 터져요! 🎈🎊
        st.snow() # 눈도 펑펑! ❄️ (선택 사항)
    else:
        st.warning("앗! 😅 아직 이 MBTI 유형에 대한 반짝이는 직업 정보가 준비되지 않았어요. ㅠㅠ 다음 업데이트 때 꼭 채워 넣을게요! ✨")

st.write("---") # 하단 구분선

st.markdown("""
<div style="text-align: center; font-size: 0.9em; color: #888;">
    <p>🚀 이 앱은 <strong><a href="https://streamlit.io/" target="_blank" style="color: #FF69B4; text-decoration: none;">Streamlit</a></strong>으로 반짝반짝 만들어졌답니다! ✨</p>
    <p>🌈 더 많은 꿈을 담아 자신만의 멋진 앱을 만들어 보세요! 🎨💖</p>
</div>
""", unsafe_allow_html=True)
