import streamlit as st
import random
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="일차함수 그래프 퀴즈 ✏️", page_icon="📉")

st.title("📘 일차함수 그래프 퀴즈")

# 일차함수 문제 목록
functions = [
    {"text": "y = 2x + 1", "a": 2, "b": 1},
    {"text": "y = -x + 3", "a": -1, "b": 3},
    {"text": "y = 0.5x - 2", "a": 0.5, "b": -2},
    {"text": "y = -2x - 1", "a": -2, "b": -1},
    {"text": "y = x", "a": 1, "b": 0},
]

# 상태 초기화
if "current_func" not in st.session_state:
    st.session_state.current_func = random.choice(functions)
    st.session_state.check_done = False
    st.session_state.correct = None

# 문제 보여주기
func = st.session_state.current_func
st.subheader(f"👉 제시된 일차함수: **{func['text']}**")

# 학생 입력: 두 x값
x1 = st.number_input("첫 번째 x값", key="x1", step=1.0)
x2 = st.number_input("두 번째 x값", key="x2", step=1.0)

if x1 == x2:
    st.warning("⚠️ 서로 다른 두 x값을 입력하세요.")
else:
    a, b = func["a"], func["b"]
    y1 = a * x1 + b
    y2 = a * x2 + b

    # 데이터프레임 생성
    graph_data = pd.DataFrame({
        "x": [x1, x2],
        "y": [y1, y2]
    }).sort_values("x")

    st.line_chart(graph_data.set_index("x"))
    with st.expander("📊 좌표 정보 보기"):
        st.write(f"첫 번째 점: ({x1}, {y1})")
        st.write(f"두 번째 점: ({x2}, {y2})")

    # 정답 확인 버튼
    if st.button("✅ 정답 확인"):
        # 두 점이 정확히 함수 위의 점인지 확인
        correct1 = y1 == round(a * x1 + b, 2)
        correct2 = y2 == round(a * x2 + b, 2)
        if correct1 and correct2:
            st.success("🎉 정답이에요! 그래프가 올바르게 그려졌어요.")
            st.balloons()
            st.session_state.correct = True
        else:
            st.error("❌ 아쉽지만 틀렸어요. 점이 함수 위에 있지 않아요.")
            st.session_state.correct = False
        st.session_state.check_done = True

# 다시 문제 출제
if st.button("🔁 새로운 문제로 다시 도전!"):
    st.session_state.current_func = random.choice(functions)
    st.session_state.check_done = False
    st.session_state.correct = None
    st.experimental_rerun()
