import streamlit as st

st.title("10주차 스트립릿 연습")

st.info("안녕하세요. 소개페이지입니다. ~~~~")
st.error("빨간박스")
st.success("초록박스")
st.warning("노란박스")

st.header("메인페이지")
st.subheader("그다음 중제목")
st.write("모든 내용 다쓰기 가능")
st.markdown("이것은 **텍스트**쓰기")
st.latex("ax^2+c")
st.code("print('hello teachers')")
st.write("---")

st.image("1.png", width=600)
st.image("https://search.pstatic.net/sunny/?src=https%3A%2F%2Fhkicorea.godohosting.com%2Felizabeth%2520HL%2FEH061L_04.jpg&type=a340")
#st.video("https://www.youtube.com/watch?v=-UqwxCwCvF4")

st.link_button("데스모스 행렬계산기 바로가기", "http://www.desmos.com/matrix")
st.components.v1.iframe("http://www.desmos.com/matrix", 
                        height=500)
#st.link_button("유튜브로",)

