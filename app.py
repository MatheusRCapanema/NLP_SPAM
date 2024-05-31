import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Predição se uma mensagem é um spam")

mesage = st.text_input("Escreva uma mensagem")

submit = st.button("Prever")

if submit:
    prediction = model.predict([mesage])

    if prediction[0] == 'spam':
        st.error("Essa mensagem é um spam")
    else:
        st.success("Essa mensagem não é um spam")

st.balloons()