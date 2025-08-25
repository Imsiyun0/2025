import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("📘 시험 대비 스터디 플래너 (깔끔한 카드형)")

# 입력
exam_date = st.date_input("시험 날짜 선택")
daily_hours = st.number_input("하루 총 공부 가능 시간(시간)", min_value=1, max_value=24, value=5)
num_subjects = st.number_input("과목 수", min_value=1, max_value=10, value=3)

subjects = {}
for i in range(num_subjects):
    st.subheader(f"과목 {i+1}")
    subject_name = st.text_input(f"과목 이름", key=f"subj_{i}")
    is_weak = st.checkbox(f"{subject_name} 부족 과목?", key=f"weak_{i}")
    chapters_text = st.text_area(f"{subject_name} 시험 범위 (소단원 단위로 줄바꿈 입력)", key=f"chap_{i}")
    if subject_name and chapters_text:
        subjects[subject_name] = {
            "weak": is_weak,
            "chapters": [c.strip() for c in chapters_text.split("\n") if c.strip()]
        }

def convert_to_hm(minutes):
    h = int(minutes // 60)
    m = int(minutes % 60)
    if h > 0 and m > 0:
        return f"{h}시간 {m}분"
    elif h > 0:
        return f"{h}시간"
    else:
        return f"{m}분"

if st.button("📅 전체 계획표 생성"):
    today = datetime.today().date()
    days_left = (exam_date - today).days
    if days_left <= 0:
        st.error("시험 날짜는 오늘 이후로 설정해주세요!")
    elif not subjects:
        st.warning("과목과 소단원을 입력해주세요!")
    else:
        weak_bonus = 1.5
        weights = {}
        total_units_weighted = 0
        for subj, data in subjects.items():
            weight = weak_bonus if data["weak"] else 1
            weights[subj] = weight
            total_units_weighted += len(data["chapters"]) * weight

        chapter_indices = {subj:0 for subj in subjects.keys()}
        for day in range(days_left):
            date_str = (today + timedelta(days=day)).strftime("%Y-%m-%d")
            st.markdown(f"### 📅 {date_str}")
            total_day_minutes = daily_hours * 60
            for subj, data in subjects.items():
                if not data["chapters"]:
                    continue
                weight = weights[subj]
                minutes = total_day_minutes * (len(data["chapters"]) * weight) / total_units_weighted
                idx = chapter_indices[subj] % len(data["chapters"])
                st.markdown(f"**{subj}** - {data['chapters'][idx]} → ⏰ {convert_to_hm(minutes)}")
                chapter_indices[subj] += 1
            st.markdown(f"**총 공부시간:** ⏰ {convert_to_hm(total_day_minutes)}")
            st.markdown("---")
