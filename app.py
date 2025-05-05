import streamlit as st
import gspread
import pandas as pd

st.title("RetsuStatus")

@st.cache_resource
def load_google_sheet():
    CREDS = st.secrets['gsp_secrets']['my_project_settings']
    gc = gspread.service_account_from_dict(CREDS)
    return gc.open('Retsupurae Library').sheet1 # gmail account

rl = load_google_sheet()
df = pd.DataFrame(rl.get_all_records())
for i, row in df.iterrows():
    for col in row.columns:
        st.write(col)
        st.write(row[col])

