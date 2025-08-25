import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import math

st.title("📘 스마트 스터디 플래너")

st.write("과목, 시험 날짜, 시험 범위, 하루 공부 가능 시간을 입력하면 맞춤형 공부 계획을 세워줍니다!")
st.write("⚠️ 시험 범위는 **한 단원의 소단원까지 정확하게 입력**해주세요!")

# 입력
subject = st.text_input("과목명")
exam_date = st.date_input("시험 날짜")
topics_input = st.text_area("시험 범위 (소단원 단위로 줄바꿈해서 입력)", height=150)
daily_study_hours = st.number_input("하루 총 공부 가능 시간 (시간 단위)", min_value=1, max_value=24, value=3)

if st.button("공부 계획 세우기"):
    if subject and exam_date and topics_input:
        today = datetime.today().date()
        days_left = (exam_date - today).days

        if days_left <= 0:
            st.error("시험 날짜는 오늘 이후여야 합니다!")
        else:
            topics = topics_input.split("\n")
            total_topics = len(topics)

            # 총 공부 시간 (분 단위)
            total_available_minutes = days_left * daily_study_hours * 60

            # 한 소단원당 배정 시간
            minutes_per_topic = total_available_minutes / total_topics

            # 날짜별 계획표 생성
            plan = []
            current_day = today
            topic_index = 0

            for day in range(days_left):
                day_plan = []
                remaining_minutes = daily_study_hours * 60

                while remaining_minutes > 0 and topic_index < total_topics:
                    allocated = min(minutes_per_topic, remaining_minutes)
                    hours = int(allocated // 60)
                    mins = int(allocated % 60)
                    day_plan.append((topics[topic_index], f"{hours}시간 {mins}분"))
                    remaining_minutes -= allocated
                    topic_index += 1

                total_day_hours = int((daily_study_hours * 60 - remaining_minutes) // 60)
                total_day_mins = int((daily_study_hours * 60 - remaining_minutes) % 60)

                plan.append({
                    "날짜": current_day.strftime("%Y-%m-%d"),
                    "공부 계획": "\n".join([f"- {t[0]} ({t[1]})" for t in day_plan]),
                    "총 공부시간": f"{total_day_hours}시간 {total_day_mins}분"
                })

                current_day += timedelta(days=1)

            df = pd.DataFrame(plan)
            st.success(f"✅ {subject} 시험까지 {days_left}일 남았습니다. 맞춤형 계획표를 확인하세요!")
            st.dataframe(df, use_container_width=True)

    else:
        st.warning("모든 입력값을 채워주세요!")
