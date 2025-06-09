import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="MBTI 비교 결과 🐶", page_icon="🦊")

st.title("📊 친구들이 보는 나의 MBTI 결과")

name = st.text_input("이름을 입력해주세요 (친구 링크 생성 시 사용한 이름)", "")

animal_emojis = [
    "🐶", "🐱", "🐰", "🦊", "🐻", "🐼", "🐯", "🦁",
    "🐮", "🐷", "🐸", "🐵", "🦄", "🐙", "🦋", "🐥"
]

file_path = f"data/{name}_votes.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    counts = df["MBTI"].value_counts().sort_values(ascending=False)
    
    st.subheader("💬 친구들이 생각하는 MBTI 분포")
    for i, (mbti, count) in enumerate(counts.items()):
        emoji = animal_emojis[i % len(animal_emojis)]
        st.markdown(f"{emoji} **{mbti}**: {count}표")
    
    st.bar_chart(counts)
else:
    st.warning("아직 친구들의 투표가 없거나 이름이 잘못되었어요! 😢")
