import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("📅 스마트 시험 대비 공부 계획 생성기 (단원/소단원별)")

# 1. 사용자 입력: 과목과 시험 날짜
st.header("시험 일정 및 범위 입력")
st.markdown("👉 과목별로 **시험 날짜**와 **시험 범위(단원/소단원까지 구체적으로)** 입력해주세요.")
st.markdown("예시: `1단원-1, 1단원-2, 2단원-1, 2단원-2` 처럼 소단원까지 정확히 입력하면 더 세밀한 계획을 세울 수 있어요!")

subjects = st.text_area("과목 이름을 쉼표(,)로 구분해서 입력하세요 (예: 수학, 영어, 과학)")
subject_list = [s.strip() for s in subjects.split(",") if s.strip() != ""]

exam_dates = []
exam_units = []  # 단원/소단원 범위 입력
for subject in subject_list:
    date = st.date_input(f"{subject} 시험 날짜 선택")
    exam_dates.append(date)
    units = st.text_area(f"{subject} 시험 범위 입력 (단원/소단원까지 구체적으로, 예: 1단원-1, 1단원-2, 2단원-1)")
    exam_units.append([u.strip() for u in units.split(",") if u.strip() != ""])

# 2. 사용자 입력: 하루 공부 가능 시간
study_hours = st.number_input("하루 총 공부 가능 시간 (시간 단위)", min_value=1, max_value=24, value=3)

if st.button("📊 스마트 단원/소단원별 공부 계획 생성"):
    today = datetime.today().date()
    
    # 남은 일수 계산
    remaining_days = [(exam - today).days for exam in exam_dates]
    
    # 남은 일수가 0 이하인 과목 제외
    filtered_subjects = [(subject_list[i], remaining_days[i], exam_units[i]) 
                         for i in range(len(subject_list)) if remaining_days[i] > 0]
    
    if not filtered_subjects:
        st.warning("모든 시험이 오늘이거나 이미 지났습니다!")
    else:
        plan = []
        for subject, days_left, units in filtered_subjects:
            num_units = len(units)
            if num_units == 0:
                continue
            daily_hours_per_unit = round(study_hours / num_units, 2)
            
            for d in range(days_left):
                date = today + timedelta(days=d)
                # 날짜별로 단원 순환 공부 계획
                unit = units[d % num_units]  
                plan.append({
                    "날짜": date,
                    "과목": subject,
                    "단원/소단원": unit,
                    "공부 시간 (시간)": daily_hours_per_unit
                })
        
        df = pd.DataFrame(plan)

        st.header("✅ 스마트 단원/소단원별 공부 계획표")

        # 날짜별로 묶어서 출력
        grouped = df.groupby("날짜")
        for date, group in grouped:
            st.subheader(f"📅 {date}")
            for _, row in group.iterrows():
                st.write(f"- {row['과목']} | {row['단원/소단원']} | {row['공부 시간 (시간)']} 시간")
