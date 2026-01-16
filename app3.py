import streamlit as st
import joblib
from PIL import Image
def main():
    st.markdown("<h3 style='text-align:center; color:red;'>Heart_Failure</h3>",
    unsafe_allow_html=True)
    img = Image.open("download (1).jpg")
    st.image(img, width=500)
    age=st.number_input("enter the age:",value=0.0)
    anaemia=st.selectbox("select value",[0,1],key="anaemia")
    creatinine=st.number_input("enter the creatine:",step=1)
    diabetics=st.selectbox("select value",[0,1],key="diabetics")
    ejection_fraction=st.number_input("enter the ejection_fraction:",step=1)
    blood_pressure=st.number_input("enter the blood_pressure:",step=1)
    platelets=st.number_input("enter the platelets:",value=0.0)
    serum_creatine=st.number_input("enter the serum_creatine:",value=0.0)
    serum_sodium=st.number_input("enter",step=1)
    sex=st.selectbox("enter the sex:",[0,1],key="sex")
    smoking=st.selectbox("enter the smoking:",[0,1],key="smoking")
    time=st.number_input("enter the time:",step=1)
    features=[age,anaemia,creatinine,diabetics,ejection_fraction,blood_pressure,platelets,serum_creatine,serum_sodium,sex,smoking,time]
    model=joblib.load("model.pkl")
    pred = st.button("predict")
    if pred:
        result=model.predict([features])
        if result==1:
            st.write(":red[PATIENT DIED]")
        else:
            st.write(":green[PATIENT SURVIVED]")


main()