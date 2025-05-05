import streamlit as st
import gdown
import pandas as pd

st.title("RetsuStatus")

@st.cache_resource
def download_google_sheet():
    url = "https://docs.google.com/spreadsheets/d/11eOF_az4j1eJoARD6T791TAV8nV7DyBvJSJlW-mNr1w/edit?usp=sharing"
    output = "retsu.csv"
    gdown.download(url=url, output=output, fuzzy=True)

df = pd.read_csv("retsu.csv")
for i, row in df.iterrows():
    for col in row.columns:
        st.write(col)
        st.write(row[col])

