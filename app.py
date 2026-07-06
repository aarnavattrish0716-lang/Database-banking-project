import streamlit as st
from auth import login
st.set_page_config(
    page_title="Banking Management System",
    page_icon="🏦",
    layout="centered"
)
st.title("🏦 Banking Management System")
st.write("Login to continue")

username=st.input_text("Username")
password=st.input_text(
    "Password",
    type="Password"
)
if st.button("Login"):
    user=login(username,password)
    if user:
        st.success("Login successful")
        st.session_state.logged_in=True
        st.session_state.user_id=user["user_id"]
        st.session_state.username=user["user_name"]
        st.session_state.role=user["role"]
        if st.session_state.role=="ADMIN":
            st.write("Welcome Admin")
        if st.session_state.role=="STAFF":
            st.write("Welcome Staff")
        else:
            st.write("Welcome Customer")
    else:
        st.error("Invalid Username or Password or Role")
