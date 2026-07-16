import streamlit as st
import modules.staff_fun as md
from datetime import datetime

st.title("👨‍💼 Staff Dashboard")

now = datetime.now()

st.markdown(
f"""
### Welcome, {st.session_state.username}

📅 {now.strftime('%A, %d %B %Y')}

🕒 {now.strftime('%I:%M %p')}
"""
)

counts = md.get_staff_dashboard(
    st.session_state.branch_id
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👥 Customers",
        counts["customers"],
        border=True
    )

with col2:
    st.metric(
        "💳 Accounts",
        counts["accounts"],
        border=True
    )

with col3:
    st.metric(
        "🔄 Transactions",
        counts["transactions"],
        border=True
    )

if st.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()