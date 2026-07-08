import streamlit as st
import modules.admin_fun as md
st.title("🏦 Branch Management")
with st.form("branch_form"):
    branch_name=st.text_input("Branch Name")
    location=st.text_input("Location")
    submit=st.form_submit_button("Add branch")
# We are using with here because otherwise we have to mention which form these text_input belongs to
# form = st.form("branch_form")
# branch_name = form.text_input("Branch Name")
# location = form.text_input("Location")
# submit = form.form_submit_button("Add Branch")


