import streamlit as st
import modules.customer_fun as md

st.title("👤 Customer Dashboard")

st.write(f"Welcome **{st.session_state.username}**")

account = md.get_customer_dashboard(
    st.session_state.user_id
)

if account["Total_Accounts"] == 0:

    st.warning(
        "No accounts have been assigned to you yet. Please contact your branch."
    )

else:

    loan = md.get_customer_loans(
        st.session_state.user_id
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏦 Total Accounts",
            account["Total_Accounts"],
            border=True
        )

    with col2:
        st.metric(
            "✅ Active Accounts",
            account["Active_Accounts"],
            border=True
        )

    with col3:
        st.metric(
            "💰 Active Balance",
            f"₹{account['Total_Balance']:.2f}",
            border=True
        )
    col4, col5=st.columns(2)
    with col4:
        st.metric(
            "📄 Active Loans",
            loan["Active_Loans"],
            border=True
        )

    with col5:
        st.metric(
            "⏳ Pending Loans",
            loan["Pending_Loans"],
            border=True
        )
if st.button("Logout"):

    st.session_state.logged_in = False
    st.rerun()