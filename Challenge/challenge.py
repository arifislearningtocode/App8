import streamlit as st
import plotly.express as px
import glob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

files = glob.glob("diary/*.txt")


d = {}
print(files)
for i in files:
    with open(f'{i}', 'r') as file:
        w = file.read()
        d[i] = w

analyzer = SentimentIntensityAnalyzer()
for i in d:
    scores = analyzer.polarity_scores(d[i])
    print(scores)

lol = [analyzer.polarity_scores(d[i]) for i in d]
print(lol)

positivity = [i['pos'] for i in lol]
print(positivity)

negativity = [i['neg'] for i in lol]
print(negativity)

data = [i.strip('diary\\').strip('.txt') for i in files]

st.header("Diary Tone")
st.subheader("Positivity")
figure = px.line(x=data, y=positivity, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=data, y=negativity, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(figure)
