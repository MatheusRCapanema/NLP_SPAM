import os

import streamlit as st
import pickle


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'model.pkl')
if os.path.exists(file_path):
    model = pickle.load(open(file_path, 'rb'))
else:
    print(f"File {file_path} does not exist.")

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