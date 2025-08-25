import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("📒 스마트 스터디 플래너")

# 1. 사용자 입력
st.header("시험 일정 및 범위 입력")
st.markdown("👉 과목별로 **시험 날짜**와 **시험 범위(단원/소단원까지 구체적으로)** 입력해주세요.")
st.markdown("예시: `1단원-1, 1단원-2, 2단원-1, 2단원-2` 처럼 소단원까지 정확히 입력하면 더 세밀한 계획을 세울 수 있어요!")

subjects = st.text_area("과목 이름을 쉼표(,)로 구분해서 입력하세요 (예: 수학, 영어, 과학)")
subject_list = [s.strip() for s in subjects.split(",") if s.strip() != ""]

exam_dates = []
exam_units = []  # 단원/소단원 입력
for subject in subject_list:
    date = st.date_input(f"{subject} 시험 날짜 선택")
    exam_dates.append(date)
    units = st.text_area(f"{subject} 시험 범위 입력 (단원/소단원까지, 예: 1단원-1, 1단원-2, 2단원-1)")
    exam_units.append([u.strip() for u in units.split(",") if u.strip() != ""])

# 2. 하루 공부 시간 입력
study_hours = st.number_input("하루 총 공부 가능 시간 (시간 단위)", min_value=1, max_value=24, value=3)

# ⏰ 소수점 → 시간+분 변환 함수
def convert_hours_to_hm(hours_float):
    h = int(hours_float)  # 정수 부분 = 시간
    m = int(round((hours_float - h) * 60))  # 소수점 부분 = 분
    if h > 0 and m > 0:
        return f"{h}시간 {m}분"
    elif h > 0:
        return f"{h}시간"
    else:
        return f"{m}분"

if st.button("📊 스터디 플래너 생성"):
    today = datetime.today().date()
    remaining_days = [(exam - today).days for exam in exam_dates]

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
            daily_hours_per_unit = study_hours / num_units  # 소수점 그대로 계산

            for d in range(days_left):
                date = today + timedelta(days=d)
                unit = units[d % num_units]
                plan.append({
                    "날짜": date,
                    "과목": subject,
                    "단원/소단원": unit,
                    "공부 시간(원시)": daily_hours_per_unit,
                    "공부 시간": convert_hours_to_hm(daily_hours_per_unit)
                })

        df = pd.DataFrame(plan)

        st.header("📒 스터디 플래너")

        # 날짜별 카드 형식 출력
        grouped = df.groupby("날짜")
        for date, group in grouped:
            # 하루 총 공부시간(소수점 합 → h, m 변환)
            total_hours = group["공부 시간(원시)"].sum()
            total_time_str = convert_hours_to_hm(total_hours)

            with st.container():
                st.markdown(
                    f"""
                    <div style="
                        background-color:#fdf6e3;
                        padding:20px;
                        border-radius:15px;
                        margin-bottom:15px;
                        box-shadow:2px 2px 8px rgba(0,0,0,0.1);
                    ">
                        <h3 style="margin:0; color:#2c3e50;">📅 {date}</h3>
                        <p style="margin:5px 0; font-weight:bold; color:#d35400;">총 공부시간: ⏰ {total_time_str}</p>
                        <ul style="font-size:16px; line-height:1.6; color:#34495e;">
                    """, unsafe_allow_html=True
                )
                for _, row in group.iterrows():
                    st.markdown(
                        f"<li>{row['과목']} | {row['단원/소단원']} | ⏰ {row['공부 시간']}</li>",
                        unsafe_allow_html=True
                    )
                st.markdown("</ul></div>", unsafe_allow_html=True)
