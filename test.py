import streamlit as st
import pandas as pd

st.title("📘 맞춤형 스터디 플래너")

# 1. 기본 입력
st.sidebar.header("기본 설정")
total_time = st.sidebar.number_input("하루 총 공부 가능 시간 (시간 단위)", min_value=1, max_value=24, value=5)
deficient_subject = st.sidebar.text_input("부족한 과목 (우선 배정)")

# 2. 과목 입력
st.header("과목별 시험 범위 입력")
subjects = {}
num_subjects = st.number_input("과목 수를 입력하세요", min_value=1, max_value=10, value=3)

for i in range(num_subjects):
    st.subheader(f"과목 {i+1}")
    subject_name = st.text_input(f"과목 {i+1} 이름")
    if subject_name:
        st.info("📌 시험 범위를 소단원 단위로 정확히 입력해주세요.")
        chapters = st.text_area(f"{subject_name} 시험 범위 (소단원 단위로 줄바꿈 입력)")
        if chapters:
            subjects[subject_name] = chapters.split("\n")

# 3. 시간 분배 로직
if st.button("📅 공부 계획 세우기"):
    if subjects:
        # 총 소단원 개수
        total_chapters = sum(len(chapters) for chapters in subjects.values())

        # 시간 배분 단위 (기본)
        base_minutes = (total_time * 60) / total_chapters

        plan = []

        for subject, chapters in subjects.items():
            for chap in chapters:
                minutes = base_minutes
                # 부족한 과목이면 가중치 +50%
                if subject == deficient_subject:
                    minutes *= 1.5
                hours = int(minutes // 60)
                mins = int(minutes % 60)
                plan.append([subject, chap, f"{hours}시간 {mins}분"])

        df = pd.DataFrame(plan, columns=["과목", "소단원", "예상 공부 시간"])

        st.success("📖 오늘의 맞춤형 스터디 플래너")
        st.dataframe(df, use_container_width=True)

        # 총합
        total_minutes = sum([(total_time*60)/total_chapters * (1.5 if subject==deficient_subject else 1) 
                             for subject, chapters in subjects.items() for _ in chapters])
        total_hours = int(total_minutes // 60)
        total_mins = int(total_minutes % 60)
        st.subheader(f"🕒 총 공부 시간: {total_hours}시간 {total_mins}분")

    else:
        st.warning("과목과 시험 범위를 입력해주세요!")
