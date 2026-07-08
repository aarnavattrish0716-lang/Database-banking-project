import streamlit as st
from auth import login

st.set_page_config(
    page_title="Banking Management System",
    page_icon="🏦",
    layout="centered"
)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    st.title("🏦 Banking Management System")
    st.write("Login to continue")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = login(username, password)

        if user:

            st.session_state.logged_in = True
            st.session_state.user_id = user["user_id"]
            st.session_state.username = user["user_name"]
            st.session_state.role = user["role"]

            st.rerun() # So that when user successful logged in we will rerun the script and now will enter else (2) if we don't use rerun and remove else (2) then even when else(1) runs it will open navigation   

        else: #1

            st.error("Invalid Username or Password")

else: #2

    if st.session_state.role == "ADMIN":
        ## If user is admin then only these pages will be in sidebar navigation and default screen is the first screen in the 
        pages = [
            st.Page("admin/1_home.py", title="Dashboard", icon="🏠"),
            st.Page("admin/2_users.py", title="Users", icon="👥"),
            st.Page("admin/3_accounts.py", title="Accounts", icon="🏦"),
            st.Page("admin/4_branches.py", title="Branches", icon="🌍"),
            st.Page("admin/5_loans.py", title="Loans", icon="💰"),
            st.Page("admin/6_transactions.py", title="Transactions", icon="📄"),
        ]

    elif st.session_state.role == "STAFF":

        pages = [
            st.Page("staff/1_home.py", title="Dashboard", icon="🏠"),
            st.Page("staff/2_deposit.py", title="Deposit", icon="💵"),
            st.Page("staff/3_withdraw.py", title="Withdraw", icon="💸"),
            st.Page("staff/4_transfer.py", title="Transfer", icon="🔁"),
        ]

    else:

        pages = [
            st.Page("customer/1_home.py", title="Dashboard", icon="🏠"),
            st.Page("customer/2_accounts.py", title="My Accounts", icon="🏦"),
            st.Page("customer/3_transfer.py", title="Transfer", icon="🔁"),
            st.Page("customer/4_transactions.py", title="Transactions", icon="📄"),
        ]

    pg = st.navigation(pages)
    pg.run() #This loads whichever page the user clicked. 



