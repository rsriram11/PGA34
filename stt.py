import streamlit as st
import pandas as pd
import pickle

st.title('Iris Prediction')
st.write('My first streamlit application')

sl = float(st.number_input('Enter Sepal Length'))
sw = float(st.number_input('Enter Sepal Width'))
pl = float(st.number_input('Enter petal Length'))
pw = float(st.number_input('Enter petal Width'))

if st.button('predict?'):
    st.write('processing')
    st.write('Please build your logic here!!!')
    with open('model.pkl', 'rb') as models:
        pred_model = pickle.load(models)
        predicted_value = pred_model.predict([[sl,sw,pl,pw]])
        st.write(f'predicted value is {predicted_value}')