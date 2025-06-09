import streamlit as st

st.set_page_config(page_title="나의 MBTI와 친구들의 생각 비교하기 🧠💬", page_icon="🐾")

st.title("🧠 내가 생각하는 나의 MBTI는?")
my_mbti = st.selectbox("당신이 생각하는 자신의 MBTI를 선택하세요!", [
    "INTJ", "INTP", "ENTP", "ENTJ",
    "INFJ", "INFP", "ENFP", "ENFJ",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

if st.button("📤 친구에게 MBTI 투표 요청하기"):
    st.success("✅ 링크를 복사해서 친구들에게 보내세요!")
    st.code(f"http://localhost:8501/Friends_MBTI?name=YourName")  # 실제 배포 시 URL로 변경
