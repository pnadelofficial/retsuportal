import streamlit as st
import gdown
import pandas as pd

st.title("RetsuStatus")

@st.cache_resource
def download_google_sheet():
    url = "https://docs.google.com/spreadsheets/d/11eOF_az4j1eJoARD6T791TAV8nV7DyBvJSJlW-mNr1w/edit?usp=sharing"
    output = "retsu.xlsx"
    gdown.download(url=url, output=output, fuzzy=True)

download_google_sheet()
df = pd.read_excel("retsu.xlsx")
for i, row in df.iterrows():
    row = row.fillna("N/A")
    with st.expander(row['Title']):
        st.write(f"Date of Upload: {row['Date of Upload']}")
        st.write(f"RPers: {row['RPers']}")
        st.write(f"LPer: {row['LPer']}")
        # st.write(f"Video Game: {row['Video Game']}")
        st.write(f"Console: {row['Console']}")
        st.write(f"Description: {row['Description']}")
        st.video(row['URL'])

