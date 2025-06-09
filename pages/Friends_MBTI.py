import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="친구 MBTI 투표 🧑‍🤝‍🧑", page_icon="🐻")

st.title("👀 친구가 보는 너의 MBTI는?")
name = st.query_params.get("name", "Unknown")

mbti = st.selectbox(f"{name}의 MBTI는 뭐라고 생각해?", [
    "INTJ", "INTP", "ENTP", "ENTJ",
    "INFJ", "INFP", "ENFP", "ENFJ",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

# 간단한 CSV 저장 (로컬에서만 사용 가능)
file_path = f"data/{name}_votes.csv"
os.makedirs("data", exist_ok=True)

if st.button("📩 MBTI 투표 제출하기"):
    new_vote = pd.DataFrame({"MBTI": [mbti]})
    if os.path.exists(file_path):
        old = pd.read_csv(file_path)
        df = pd.concat([old, new_vote], ignore_index=True)
    else:
        df = new_vote
    df.to_csv(file_path, index=False)
    st.success("투표가 완료되었습니다! 🎉")
