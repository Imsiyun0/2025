import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("📘 AI 스터디 플래너")
st.write("시험 과목, 시험 날짜, 시험 범위를 입력하면 **자동으로 공부 계획표**를 생성해줍니다.")
st.write("👉 한 단원 안에 있는 **소단원까지 정확히 입력**해주세요!")

# 입력 폼
with st.form("study_form"):
    subjects = st.text_area("과목과 시험 범위를 입력하세요 (예: 수학 - 확률과 통계 단원, 영어 - Reading Unit 1~3)").split("\n")
    exam_date = st.date_input("시험 날짜를 입력하세요")
    daily_available_hours = st.number_input("하루 총 공부 가능한 시간(시간)", min_value=1, max_value=24, value=5)
    weak_subjects = st.text_area("부족한 과목을 입력하세요 (예: 수학, 영어)").split("\n")
    submitted = st.form_submit_button("계획표 생성")

if submitted:
    today = datetime.today().date()
    days_left = (exam_date - today).days

    if days_left <= 0:
        st.error("시험 날짜는 오늘 이후로 설정해야 합니다!")
    else:
        st.success(f"시험까지 남은 기간: **{days_left}일**")

        # 시험 범위를 세부 단원으로 분리
        study_plan = []
        subject_units = {}

        for subj in subjects:
            if "-" in subj:
                subject, units = subj.split("-", 1)
                units = [u.strip() for u in units.split(",")]
                subject_units[subject.strip()] = units

        # 부족 과목 가중치 반영
        weights = {}
        for subj in subject_units.keys():
            if subj in weak_subjects:
                weights[subj] = 2  # 부족한 과목은 가중치 2배
            else:
                weights[subj] = 1

        total_units = sum(len(units) * weights[subj] for subj, units in subject_units.items())

        # 단위 시간 계산
        total_minutes_per_day = daily_available_hours * 60
        minutes_per_unit = (days_left * total_minutes_per_day) / total_units

        current_day = today

        for day in range(days_left):
            day_plan = []
            total_day_minutes = 0
            for subj, units in subject_units.items():
                for unit in units:
                    # 부족 과목은 단원 당 시간을 늘림
                    unit_minutes = minutes_per_unit * weights[subj]
                    total_day_minutes += unit_minutes
                    hours = int(unit_minutes // 60)
                    mins = int(unit_minutes % 60)
                    day_plan.append(f"{subj} - {unit} ({hours}시간 {mins}분)")
            study_plan.append({
                "날짜": current_day.strftime("%m/%d"),
                "계획": "\n".join(day_plan),
                "총 공부 시간": f"{int(total_day_minutes//60)}시간 {int(total_day_minutes%60)}분"
            })
            current_day += timedelta(days=1)

        # DataFrame 생성
        df = pd.DataFrame(study_plan)

        st.subheader("📅 스터디 플래너")
        st.dataframe(df, use_container_width=True)
