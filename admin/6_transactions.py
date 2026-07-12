import streamlit as st
import pandas as pd
import modules.admin_fun as md
st.title("📄 Transaction Management")
st.divider()
st.subheader("📋 Transaction History")
df=pd.DataFrame(md.get_all_transactions())
st.divider()
st.subheader("🔍 Search / Filter")
with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        search_name=st.text_input("Search Customer by name")
    with col2:
        search_account_id=st.text_input("Search by account_id")#Input type is str
if search_name:
    filtered=df[df["user_name"].str.lower().str.startswith(search_name.lower())]
    st.dataframe(filtered,hide_index=True,width="stretch")
elif search_account_id:
    filtered=df[df["account_id"].astype(str).str.startswith(search_account_id)]
    st.dataframe(filtered,hide_index=True,width="stretch")
else:
    filtered=df
    st.dataframe(filtered,hide_index=True,width="stretch")