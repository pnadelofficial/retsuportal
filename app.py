import streamlit as st
import gspread
import pandas as pd

st.title("Retsupurae Library")
# retsupurae by the numbers

print(st.secrets.gsp_secrets)

credentials = {
    "type":st.secrets.gsp_secrets.type,
    "project_id":st.secrets.gsp_secrets.project_id,
    "private_key_id":st.secrets.gsp_secrets.private_key_id,
    "private_key":st.secrets.gsp_secrets.private_key,
    "client_email":st.secrets.gsp_secrets.client_email,
    "client_id":st.secrets.gsp_secrets.client_id,
    "auth_uri":st.secrets.gsp_secrets.auth_uri,
    "token_uri":st.secrets.gsp_secrets.token_uri,
    "auth_provider_x509_cert_url":st.secrets.gsp_secrets.auth_provider_x509_cert_url,
    "client_x509_cert_url":st.secrets.gsp_secrets.client_x509_cert_url,
    "universe_domain":st.secrets.gsp_secrets.universe_domain
}

@st.cache_resource
def access_google_sheet():
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open("Retsupurae Library").sheet1
    data = sh.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    return df

df = access_google_sheet()
for c in df.columns:
    print(f"**{c}**")
for i, row in df.iterrows():
    row = row.fillna("N/A")
    with st.expander(row['Title']):
        st.write(f"Date of Upload: {row['Date of Upload']}")
        st.write(f"RPers: {row['RPers']}")
        st.write(f"LPer: {row['LPer']}")
        st.write(f"Video Game: {row['Video Game ']}")
        st.write(f"Console: {row['Console']}")
        st.write(f"Description: {row['Video Description']}")
        if row['URL'] == "N/A":
            st.video(row['URL'])

