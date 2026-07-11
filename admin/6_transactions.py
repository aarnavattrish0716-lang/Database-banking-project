import streamlit as st
import modules.admin_fun as md
st.title("📄 Transaction Management")
st.divider()
st.subheader("📋 Transaction History")
data=md.get_all_transactions()
st.dataframe(data,hide_index=True)
st.divider()
st.subheader("🔍 Search / Filter")
