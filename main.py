import streamlit as st

# 🎬 MBTI에 따른 추천 영화 딕셔너리
movie_recommendations = {
    "INTJ": ("인터스텔라", "우주의 신비를 추적하는 시간 여행! 🚀🧠"),
    "INTP": ("이미테이션 게임", "천재 튜링의 암호 해독 이야기! 💻🧩"),
    "ENTP": ("마션", "화성에서 살아남기! 🔥🌌"),
    "ENTJ": ("뷰티풀 마인드", "천재 수학자의 내면 세계를 그린 감동 실화 🎓🧮"),
    "INFJ": ("컨택트", "언어와 시간의 경계를 넘는 감성 SF 👽🕰️"),
    "INFP": ("빅 히어로", "로봇과 우정, 그리고 히어로! 🤖❤️"),
    "ENFP": ("백 투 더 퓨처", "시간을 넘나드는 청춘 어드벤처! ⏳🚗"),
    "ENFJ": ("파이 이야기", "신비로운 바다 위의 생존과 철학 🌊🐅"),
    "ISTJ": ("굿 윌 헌팅", "숨겨진 천재성과 성장 이야기 ✍️📚"),
    "ISFJ": ("히든 피겨스", "NASA 뒤의 숨은 영웅들 🚀💪"),
    "ESTJ": ("소셜 네트워크", "페이스북의 창업 이야기와 전략 📱💼"),
    "ESFJ": ("코다", "과학은 아니지만, 따뜻한 감성영화로 균형 추천 🎵🧡"),
    "ISTP": ("인셉션", "꿈과 수학적 구조가 결합된 SF 명작 🌀🛌"),
    "ISFP": ("월-E", "환경과 로봇의 사랑 이야기 🌍🤖"),
    "ESTP": ("쥬라기 공원", "생명공학의 끝, 공룡의 부활! 🦖🔬"),
    "ESFP": ("매트릭스", "현실과 가상, 선택의 수학적 구조 🕶️🔢"),
}

st.set_page_config(page_title="MBTI 영화 추천기 🎥", page_icon="🎬")

st.title("🎥 MBTI 맞춤 수학·과학 명작 영화 추천기")
st.markdown("당신의 **MBTI 유형**을 선택해보세요! 🍿")

# 👉 selectbox로 MBTI 목록 선택
mbti_list = list(movie_recommendations.keys())
selected_mbti = st.selectbox("MBTI 유형 선택", mbti_list, index=mbti_list.index("INTP"))

if st.button("🎬 영화 추천 받기"):
    title, description = movie_recommendations[selected_mbti]
    st.balloons()  # 🎈 풍선 효과!
    st.success(f"**🎞️ 추천 영화: {title}**\n\n{description}")

st.caption("💡 참고: 이 추천은 MBTI 성향과 영화 테마를 창의적으로 매칭한 것이며, 개인의 취향과 다를 수 있어요!")
