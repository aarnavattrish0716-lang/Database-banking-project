import streamlit as st

st.title("🏦 Admin Dashboard")

st.write(f"Welcome {st.session_state.username}")

if st.button("Logout"):
    st.session_state.logged_in=False
    st.rerun()