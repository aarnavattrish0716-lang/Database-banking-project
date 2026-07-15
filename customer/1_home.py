import streamlit as st
import modules.customer_fun as md

st.title("👤 Customer Dashboard")

st.write(f"Welcome {st.session_state.username}")
account = md.get_customer_dashboard(st.session_state.user_id)
loan=md.get_customer_loans(st.session_state.user_id)
if account:
        st.metric("Total Accounts",f"{account["Total_Accounts"]}",border=True)
        st.metric("Balance", f"₹{account['Total_Balance']}",border=True)
if loan:
        st.metric("Loans",f"{loan["Total_Loans"]}",border=True)
else:
    st.warning("No accounts found.")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()