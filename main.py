import streamlit as st

st.set_page_config(page_title="운동 추천기 🏋️", page_icon="🏃")

st.title("🏃‍♀️ 취향 기반 운동 추천 서비스")
st.markdown("5단계 취향을 선택하면, 당신에게 딱 맞는 운동을 추천해드려요! 🎯")

# --- Step 1: 실내 vs 실외
step1 = st.radio("1️⃣ 당신은 어디서 운동하는 걸 더 좋아하나요?", ["실내에서 운동하기 🏠", "실외에서 운동하기 🌳"])

# --- Step 2: 혼자 vs 함께
step2 = st.radio("2️⃣ 운동은 어떤 방식이 좋나요?", ["혼자 하는 운동 🤸‍♀️", "여럿이 함께 하는 운동 🧑‍🤝‍🧑"])

# --- Step 3: 도구 사용 여부
step3 = st.radio("3️⃣ 운동할 때 도구를 사용하는 걸 좋아하나요?", ["도구를 사용하는 운동 🏋️", "도구 없이 하는 운동 🧘"])

# --- Step 4: 운동 강도
step4 = st.radio("4️⃣ 어떤 강도의 운동을 선호하나요?", ["가벼운 강도 🌿", "중간 강도 🚶‍♂️", "강한 강도 🔥"])

# --- Step 5: 운동의 목적
step5 = st.radio("5️⃣ 운동 목적은 무엇인가요?", ["건강 관리 🫀", "스트레스 해소 🧘", "체력 향상 💪"])

# 추천 로직: 간단한 규칙 기반 (조합의 일부 예시만 포함)
def recommend_exercise():
    if step1 == "실내에서 운동하기 🏠":
        if step2 == "혼자 하는 운동 🤸‍♀️":
            if step3 == "도구 없이 하는 운동 🧘":
                return "요가 🧘‍♂️", "고요한 분위기에서 혼자 즐길 수 있는 실내 운동이에요."
            else:
                return "홈 트레이닝 (덤벨, 밴드 등) 🏋️", "집에서도 간편한 도구로 효율적인 운동 가능!"
        else:
            return "에어로빅 👯", "실내에서 다 함께 신나게 움직여보세요!"
    else:  # 실외
        if step2 == "혼자 하는 운동 🤸‍♀️":
            if step3 == "도구 없이 하는 운동 🧘":
                return "조깅 🏃‍♀️", "햇빛 받으며 혼자 달리는 조용한 시간!"
            else:
                return "사이클 🚴‍♂️", "도시나 공원을 달리는 상쾌한 기분!"
        else:
            return "축구 ⚽", "다 같이 뛰고 협동심도 기를 수 있어요!"

# 버튼 클릭 시 추천
if st.button("📌 나에게 맞는 운동 추천받기!"):
    exercise, reason = recommend_exercise()
    st.balloons()
    st.success(f"🏅 추천 운동: **{exercise}**\n\n💡 {reason}")

st.caption("💬 단순 규칙 기반 추천이며, 실제 운동은 자신의 건강 상태에 따라 선택하세요!")
