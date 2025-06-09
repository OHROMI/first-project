import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="일차함수 그래프 그리기 📉", page_icon="✏️")

st.title("📘 일차함수 그래프 그리기")

# 일차함수 후보들
functions = [
    {"text": "y = 2x + 1", "a": 2, "b": 1},
    {"text": "y = -x + 3", "a": -1, "b": 3},
    {"text": "y = 0.5x - 2", "a": 0.5, "b": -2},
    {"text": "y = -2x - 1", "a": -2, "b": -1},
    {"text": "y = x", "a": 1, "b": 0},
]

# 함수 랜덤 선택
if "selected_func" not in st.session_state:
    st.session_state.selected_func = random.choice(functions)

selected = st.session_state.selected_func
st.subheader(f"👉 제시된 일차함수: **{selected['text']}**")

# 학생이 x좌표 2개 입력
st.markdown("✏️ 두 개의 x좌표를 입력하면, 해당 함수의 그래프를 그려볼 수 있어요.")
x1 = st.number_input("첫 번째 x값", key="x1")
x2 = st.number_input("두 번째 x값 (x1과 달라야 해요!)", key="x2")

if x1 == x2:
    st.warning("⚠️ 서로 다른 두 x값을 입력해야 해요.")
else:
    # y값 계산
    a, b = selected["a"], selected["b"]
    y1 = a * x1 + b
    y2 = a * x2 + b

    # 데이터프레임 생성
    data = pd.DataFrame({
        "x": [x1, x2],
        "y": [y1, y2]
    }).sort_values("x")

    # 그래프 출력
    st.line_chart(data.set_index("x"))

    st.success(f"🎉 함수 {selected['text']}의 그래프가 그려졌어요!")

    with st.expander("📊 좌표 정보 보기"):
        st.write(f"첫 번째 점: ({x1}, {y1})")
        st.write(f"두 번째 점: ({x2}, {y2})")
