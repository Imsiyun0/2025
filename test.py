import streamlit as st

st.title("📚 시험 대비 스터디 플래너")

# 총 공부 시간 입력
total_time = st.number_input("하루 총 공부 가능 시간(시간)", min_value=1, max_value=24, value=5)

# 과목 개수 입력
num_subjects = st.number_input("과목 개수", min_value=1, max_value=10, value=3)

subjects = {}
for i in range(num_subjects):
    subject_name = st.text_input(f"과목 {i+1} 이름", key=f"subject_name_{i}")
    weak = st.checkbox(f"{subject_name} 부족 과목인가요?", key=f"weak_{i}")
    chapters = st.text_area(f"{subject_name} 시험 범위 (소단원 단위로 줄바꿈 입력)", key=f"chapters_{i}")
    
    if subject_name:
        subjects[subject_name] = {
            "weak": weak,
            "chapters": chapters.split("\n") if chapters else []
        }

if st.button("공부 계획 세우기"):
    weak_bonus = 1.5
    total_weight = 0
    weights = {}

    for subject, data in subjects.items():
        weight = weak_bonus if data["weak"] else 1
        weights[subject] = weight
        total_weight += weight

    st.subheader("📌 오늘의 공부 계획")
    for subject, data in subjects.items():
        allocated_time = (weights[subject] / total_weight) * total_time
        chapters = data["chapters"]
        if chapters:
            time_per_chapter = allocated_time / len(chapters)
            st.markdown(f"**{subject} ({allocated_time:.1f}시간)**")
            for ch in chapters:
                st.write(f"- {ch.strip()} → {time_per_chapter:.1f}시간")
        else:
            st.write(f"**{subject} ({allocated_time:.1f}시간)** (세부 범위 없음)")
