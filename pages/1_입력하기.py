import streamlit as st

classcode="123456"
code=st.text_input("강의코드를 입력하세요")
if code==classcode:
    st.success("강의코드가 일치합니다.")
else:
    st.error("강의코드가 일치하지 않습니다.")

st.subheader("다양한 인풋")
#객관식 라디오 버튼, 체크박스/ 주관식 숫자만 입력/ 슬라이더/ 파일업로드

answer=st.radio("객관식 문항",["5","6","7","8"])
if answer=="7":
    st.success("잘했어요!! 정답입니다.")
elif answer=="8":
    st.warning("이항 확인!")
else:
    st.error("다시 생각해보세요!!오답입니다.")

agree=st.checkbox("동의합니까?")
if agree==True:
    st.success("동의하셨습니다.")
elif agree==False:
    st.error("동의하지 않으셨습니다.")
else:
    st.warning("다시 생각해보세요!!")

answer2=st.text_input("이차함수를 입력해주세요.",placeholder="ex) y=x^2+2x+1")
if answer2=="y=x^2+2x+1":
    st.success("정답입니다.")
else:
    st.error("다시 생각해보세요!!오답입니다.")

answer3=st.number_input("숫자를 입력하세요",min_value=0,max_value=100,value=50,step=1)

st.write(answer3*2+1)

if st.button("확인"):
    st.success("확인되었습니다.")

#라디오버튼 문제에 대한 정답 제출하기 버튼 ->피드백
answer=st.radio("라디오버튼 문제",["5","6","7","8"])
if st.button("정답 제출"):
    if answer=="7":
        st.success("잘했어요!! 정답입니다.")
    elif answer=="8":
        st.warning("이항 확인!")
    else:
        st.error("다시 생각해보세요!!오답입니다.")

answer4=st.slider("나이를 선택해주세요",min_value=0,max_value=120,value=20,step=1)
if answer4>=60:
    st.warning("노인입니다.")
elif answer4>=20:
    st.success("성인입니다.")
else:
    st.error("청소년입니다.")

