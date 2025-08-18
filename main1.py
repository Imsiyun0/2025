import streamlit as st
from PIL import Image # Pillow 라이브러리로 이미지 처리

# 💖 이 부분은 실제 AI 모델과 추천 시스템 로직이 들어갈 자리입니다! 💖
# 현재는 가상의 분석/추천 결과를 반환합니다.

def analyze_fashion_item(image):
    """
    업로드된 옷 이미지를 분석하여 브랜드와 제품 정보를 반환하는 가상의 함수.
    실제 앱에서는 여기에 딥러닝 모델 호출 로직이 들어갑니다.
    """
    st.info("💡 AI 패션 전문가가 사진 속 옷을 분석 중입니다... 잠시만 기다려 주세요! 🧐")
    import time
    time.sleep(2) # 분석하는 척 2초 지연 ⏳

    # 가상의 분석 결과: 파일 이름에 따라 결과를 다르게 설정
    # (실제 로직에서는 이미지의 픽셀 데이터를 분석하여 인식)
    # 🌟 이미지 파일 이름 예시 (실제 앱에서는 이미지 내용으로 분석)
    # - 'nike_hoodie.jpeg'
    # - 'chanel_bag.png'
    # - 'zara_dress.jpg'
    # - 'thisisneverthat_tshirt.png'
    # - 'mardi_mercredi_sweatshirt.jpg'
    # - 'stussy_cap.webp'
    # - 'musinsa_street_style.jpeg'
    # - 'ably_daily_look.png'
    
    # 임시 파일 이름으로 가상 분석 결과 리턴 (실제 AI 모델로 교체될 부분)
    image_filename = getattr(image, 'name', 'unknown').lower()
    
    if "nike" in image_filename:
        st.success("✅ 패션 분석 완료! 스포티한 감각이 돋보이네요! 🤩")
        st.balloons()
        return "NIKE 👟", "나이키 에어포스 1", "성공! 스트릿 패션의 대표 주자죠! 😉"
    elif "chanel" in image_filename:
        st.success("✅ 패션 분석 완료! ✨ 럭셔리 아이템이네요! 💖")
        st.balloons()
        return "CHANEL ⚜️", "클래식 플랩 백", "성공! 여성들의 로망이죠! 👜"
    elif "zara" in image_filename:
        st.success("✅ 패션 분석 완료! 💃 트렌디한 아이템이네요!")
        st.balloons()
        return "ZARA 👗", "린넨 블렌드 원피스", "성공! 여름에 딱이겠어요! 💐"
    elif "thisisneverthat" in image_filename or "tnnt" in image_filename:
        st.success("✅ 패션 분석 완료! 😎 힙한 무드가 느껴지네요!")
        st.balloons()
        return "thisisneverthat ✨", "베이식 로고 맨투맨", "성공! 무신사 베스트 셀러 중 하나죠! 👍"
    elif "mardi" in image_filename:
        st.success("✅ 패션 분석 완료! 🌷 감각적인 아이템이네요!")
        st.balloons()
        return "MARDI MERCREDI 🌸", "플라워 마르디 티셔츠", "성공! 요즘 가장 핫한 브랜드 중 하나죠! 💖"
    elif "stussy" in image_filename:
        st.success("✅ 패션 분석 완료! 🧢 스트릿 패션의 정석!")
        st.balloons()
        return "STÜSSY 🌴", "스투시 기본 로고 캡", "성공! 캐주얼 룩에 포인트 주기 좋겠어요! 🔥"
    elif "musinsa" in image_filename or "street" in image_filename:
        st.success("✅ 패션 분석 완료! 🚶‍♀️🚶‍♂️ 무신사에서 자주 볼 수 있는 스타일이네요!")
        st.balloons()
        return "MUSINSA STYLING 🏙️", "오버핏 스트릿 룩", "성공! 편안하면서도 스타일리시해요! 💫"
    elif "ably" in image_filename or "daily" in image_filename:
        st.success("✅ 패션 분석 완료! 😊 에이블리에서 인기 많을 데일리룩이네요!")
        st.balloons()
        return "ABLY DAILY 💖", "여성 크롭 니트 가디건", "성공! 활용도 높은 데일리 아이템이네요! 👚"
    else: # 제품을 찾기 어려운 경우
        st.warning("⚠️ 사진 속 의류 아이템을 정확히 인식하기 어렵습니다. ㅠㅠ")
        st.snow() # 아쉬움의 눈 펑펑
        return None, None, "사진 속 의류 아이템의 특징을 정확하게 파악하기 어렵습니다."

def recommend_similar_fashion_items(analysis_result_brand, analysis_result_product):
    """
    원래 이미지 분석 결과를 바탕으로 유사한 옷/패션 아이템을 추천하는 가상의 함수.
    실제 앱에서는 여기에 추천 시스템 모델 호출 로직이 들어갑니다.
    """
    st.info("💖 시윤님의 스타일을 저격할 비슷한 패션 아이템을 찾고 있어요! ✨")
    import time
    time.sleep(3) # 추천하는 척 3초 지연 ⏳

    recommended_items = []

    if analysis_result_brand == "NIKE 👟":
        recommended_items = [
            {"아이템명": "아디다스 슈퍼스타 스니커즈 👟", "브랜드": "ADIDAS", "스타일": "클래식 스트릿 패션 👍"},
            {"아이템명": "뉴발란스 992 운동화 🏃‍♀️", "브랜드": "New Balance", "스타일": "편안함과 스타일을 동시에! 🌟"},
            {"아이템명": "MLB 로고 후드티 🧢", "브랜드": "MLB", "스타일": "트렌디한 캐주얼 스트릿 룩 🎶"},
        ]
    elif analysis_result_brand == "CHANEL ⚜️":
        recommended_items = [
            {"아이템명": "에르메스 콘스탄스 백 👜", "브랜드": "HERMÈS", "스타일": "럭셔리 무드의 상징 👑"},
            {"아이템명": "디올 레이디 백 👛", "브랜드": "DIOR", "스타일": "우아함과 클래식의 조화 💖"},
            {"아이템명": "입생로랑 로고 지갑 💳", "브랜드": "YSL", "스타일": "시크하고 모던한 매력 ✨"},
        ]
    elif analysis_result_brand == "ZARA 👗":
        recommended_items = [
            {"아이템명": "H&M 패턴 블라우스 🌸", "브랜드": "H&M", "스타일": "가성비 좋은 트렌디 아이템 💫"},
            {"아이템명": "SPAO 린넨 셔츠 👔", "브랜드": "SPAO", "스타일": "쾌적하고 시원한 데일리 룩 😊"},
            {"아이템명": "미쏘 와이드 슬랙스 👖", "브랜드": "MIXXO", "스타일": "오피스 룩부터 캐주얼까지  versatile! 👍"},
        ]
    elif analysis_result_brand == "thisisneverthat ✨":
        recommended_items = [
            {"아이템명": "LMC 오버핏 티셔츠 👕", "브랜드": "LMC", "스타일": "깔끔하고 세련된 스트릿 캐주얼 😎"},
            {"아이템명": "키르시 빅 체리 후드티 🍒", "브랜드": "KIRSH", "스타일": "귀여운 포인트로 발랄하게 🍒"},
            {"아이템명": "오아이오아이 로고 크롭 후드 👚", "브랜드": "O!O!I!", "스타일": "톡톡 튀는 컬러감이 돋보이는 팝 캐주얼 🌈"},
        ]
    elif analysis_result_brand == "MARDI MERCREDI 🌸":
        recommended_items = [
            {"아이템명": "레스트앤레크레이션 니트 가디건 🧶", "브랜드": "Rest & Recreation", "스타일": "내추럴하고 감각적인 데일리웨어 🍂"},
            {"아이템명": "프렌치시크 무드 원피스 👗", "브랜드": "LOW CLASSIC", "스타일": "우아하고 섬세한 디자이너 감성 💫"},
            {"아이템명": "이미스 볼캡 & 에코백 세트 👜", "브랜드": "emis", "스타일": "꾸안꾸 코디에 포인트 주기 🎀"},
        ]
    elif analysis_result_brand == "STÜSSY 🌴":
        recommended_items = [
            {"아이템명": "슈프림 박스 로고 티셔츠 📦", "브랜드": "Supreme", "스타일": "힙합 문화를 담은 스트릿웨어 끝판왕 👑"},
            {"아이템명": "칼하트 WIP 비니 🧑‍🏭", "브랜드": "Carhartt WIP", "스타일": "워크웨어 기반의 캐주얼 스트릿 룩 🛠️"},
            {"아이템명": "팔라스 스케이트보드 후드티 🛹", "브랜드": "Palace Skateboards", "스타일": "런던 스트릿 감성 물씬! 🇬🇧"},
        ]
    elif analysis_result_brand == "MUSINSA STYLING 🏙️":
        recommended_items = [
            {"아이템명": "코오롱 스포츠 다운자켓 🧥", "브랜드": "Kolon Sport", "스타일": "아웃도어 감성을 담은 데일리웨어 ⛰️"},
            {"아이템명": "커버낫 빅로고 후드티 🌊", "브랜드": "Covernat", "스타일": "MZ세대가 사랑하는 스트릿 캐주얼 ✨"},
            {"아이템명": "드로우핏 오버핏 셔츠 👔", "브랜드": "DRAWFIT", "스타일": "미니멀리즘 기반의 컨템포러리 웨어 📏"},
        ]
    elif analysis_result_brand == "ABLY DAILY 💖":
        recommended_items = [
            {"아이템명": "블리블리 캐주얼 밴딩 스커트 Skirt 🌷", "브랜드": "BLY BLY", "스타일": "사랑스러운 무드의 여성 데일리룩 😊"},
            {"아이템명": "로즐리 심플 베이직 니트 👚", "브랜드": "ROSLEY", "스타일": "다양한 코디에 활용하기 좋은 기본템 👍"},
            {"아이템명": "오프라인 브랜드 롱 가디건 🧣", "브랜드": "LOCAL BRAND", "스타일": "쌀쌀한 날씨에 걸치기 좋은 여리여리핏 💫"},
        ]
    else: # 제품을 못 찾았을 경우, 시윤님 관심사를 반영한 일반적인 패션/뷰티 아이템 추천 (기존과 유사)
        st.markdown("<p style='font-size:1.1em; color:#DAA520; font-weight:bold;'>🧐 사진 속 아이템이 불분명하지만, 시윤님의 스타일을 고려한 추천을 준비했어요! 💖</p>", unsafe_allow_html=True)
        recommended_items = [
            {"아이템명": "아이돌 무대 의상 오마주 코디 🎶", "브랜드": "K-Pop Inspiration", "스타일": "최애 따라잡기! 💖"},
            {"아이템명": "나만의 퍼스널 컬러 패션 컨설팅 🎨", "브랜드": "Personal Styling", "스타일": "더욱 돋보이는 나를 찾아봐요! 💫"},
            {"아이템명": "핫플레이스에서 만나는 트렌디 카페룩 ☕", "브랜드": "Café Look", "스타일": "인생샷 건지는 코디 📸"},
        ]
        
    st.success("🎉 유사 패션 아이템 추천 완료!")
    st.balloons()

    return recommended_items


st.set_page_config(
    page_title="👗 사진 속 옷 찾기 & 추천! ✨",
    page_icon="👚",
    layout="centered"
)

st.title("💖 ✨ 패션 AI, 사진 속 옷 분석 & 추천! ✨ 👚")
st.write("---")

st.markdown("""
<div style="font-size: 1.1em; text-align: center; color: #5B487A; font-weight: bold;">
    궁금한 패션 아이템이 담긴 사진을 업로드해 보세요! 🤩<br>
    제가 인공지능의 눈으로 분석해서 어떤 브랜드, 어떤 제품인지 추정해 드리고,<br>
    만약 잘 모르겠다면 당신이 좋아할 만한 비슷한 스타일의 아이템까지 추천해 드릴게요! 😉
</div>
""", unsafe_allow_html=True)

st.write("") # 간격

# 파일 업로드 위젯
uploaded_file = st.file_uploader(
    "💖 분석하고 싶은 옷/패션 아이템 이미지를 여기로 끌어다 놓거나 클릭해서 선택해 주세요! 👆",
    type=["jpg", "jpeg", "png", "webp"],
    help="JPEG, PNG, WEBP 형식의 이미지만 업로드 가능합니다."
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        image.name = uploaded_file.name # 원본 파일명 저장 (가상 분석용)

        st.write("---")
        st.subheader("🖼️ 업로드된 이미지:")
        st.image(image, caption='분석할 옷 이미지', use_column_width=True)

        st.write("") # 간격

        if st.button("🚀 패션 아이템 분석 및 추천 시작! ✨"):
            st.write("---")
            st.subheader("💡 AI 패션 분석 결과! 🧠")
            
            # 1. 패션 아이템 분석 시도
            brand, product, analysis_message = analyze_fashion_item(image)

            if brand and product: # 아이템을 정확히 찾았을 경우
                st.metric(label="✅ **추정 브랜드**", value=brand)
                st.metric(label="✅ **추정 아이템**", value=product)
                st.markdown(f"**💖 분석 메시지**: {analysis_message}")
                st.info("👍 축하합니다! 사진 속 아이템을 정확하게 인식했어요! 새로운 스타일을 찾고 싶다면 다른 사진을 업로드해 주세요! 😊")
            else: # 아이템을 찾지 못했을 경우 -> 유사 아이템 추천 로직으로 진행
                st.error(f"⚠️ **사진 속 아이템을 정확히 인식하기 어려워요. ㅠㅠ**")
                st.markdown(f"**💖 분석 메시지**: {analysis_message}")

                st.write("---")
                st.subheader("💖 시윤님의 스타일을 위한 추천은 어떠세요? ✨")
                recommended_items = recommend_similar_fashion_items(brand, product) # 분석 결과 (없으면 None) 전달
                
                if recommended_items:
                    for i, rec_item in enumerate(recommended_items):
                        st.markdown(f"**{i+1}. {rec_item['아이템명']}** ({rec_item['브랜드']}) - __{rec_item['스타일']}__")
                    st.info("💡 이 추천은 시윤님의 관심사와 유사도를 기반으로 한 **가상 추천**입니다!")
                else:
                    st.warning("아쉽게도 추천할 만한 유사 아이템을 찾지 못했어요. 😢")

        st.write("") # 간격
        st.markdown("<div style='text-align: center; color: #888;'>* 이 앱의 모든 분석 및 추천 결과는 예시이며, 실제 AI 모델이 필요합니다. *</div>", unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"오류가 발생했어요. 이미지 파일을 다시 확인해 주세요: {e} ㅠㅠ")
else:
    st.write("---")
    st.info("👆 위에 파일을 업로드하시면 옷 분석 및 추천을 시작할 수 있어요! 😊")

st.write("---")
st.markdown("""
<div style="text-align: center; font-size: 0.9em; color: #888;">
    <p>💡 이 앱은 <strong><a href="https://streamlit.io/" target="_blank" style="color: #FF69B4; text-decoration: none;">Streamlit</a></strong>으로 만들었어요! 🚀</p>
    <p>💖 시윤님의 반짝이는 아이디어를 응원합니다! ✨</p>
</div>
""", unsafe_allow_html=True)
