import streamlit as st
import pickle
import time
import numpy as np

# load the model
model = pickle.load(open('https://github.com/SemwalPrabhat/SentimentAnalysis/blob/main/pipe1.pkl', 'rb'))

st.title('Twitter Sentiment Analysis')

tweet = st.text_input('Enter your tweet')

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    if(prediction[0]==0):
        "Negative"
    if(prediction[0]==1):
        "Neutral"
    if(prediction[0]==2):
        "Positive"
    st.write(prediction[0])
