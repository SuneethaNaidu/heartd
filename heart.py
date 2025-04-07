import streamlit as st
import joblib
st.title('Heart Disease Prediction')
model= joblib.load('heart.joblib')
sex= st.number_input('Enter gender (M:0,F:1)')
cp= st.number_input('Enter cp(M:1,UM:0)')
trestbps= st.number_input('Enter trestbps')
chol= st.number_input('Enter chol')
fbs= st.number_input('Enter fbs')
restecg= st.number_input('Enter restecg')
thalach= st.number_input('Enter thalach')
exang=  st.number_input('Enter exang')
oldpeak=  st.number_input('Enter oldpeak')
slope= st.number_input('Enter slope')
ca= st.number_input('Enter ca')
thal= st.number_input('Enter thal')
if st.button('Predict Approval'):
    prediction=model.predict([[sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if prediction=='Y':
        st.text('YES')
    else:
        st.text('NO')
