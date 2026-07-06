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
            st.Page("admin/home.py", title="Dashboard", icon="🏠"),
            st.Page("admin/users.py", title="Users", icon="👥"),
            st.Page("admin/accounts.py", title="Accounts", icon="🏦"),
            st.Page("admin/branches.py", title="Branches", icon="🌍"),
            st.Page("admin/loans.py", title="Loans", icon="💰"),
            st.Page("admin/transactions.py", title="Transactions", icon="📄"),
        ]

    elif st.session_state.role == "STAFF":

        pages = [
            st.Page("staff/home.py", title="Dashboard", icon="🏠"),
            st.Page("staff/deposit.py", title="Deposit", icon="💵"),
            st.Page("staff/withdraw.py", title="Withdraw", icon="💸"),
            st.Page("staff/transfer.py", title="Transfer", icon="🔁"),
        ]

    else:

        pages = [
            st.Page("customer/home.py", title="Dashboard", icon="🏠"),
            st.Page("customer/accounts.py", title="My Accounts", icon="🏦"),
            st.Page("customer/transfer.py", title="Transfer", icon="🔁"),
            st.Page("customer/transactions.py", title="Transactions", icon="📄"),
        ]

    pg = st.navigation(pages)
    pg.run() #This loads whichever page the user clicked. 



# In Streamlit, the script reruns whenever a widget interaction occurs.

# Examples of interactions that trigger a rerun:

# ✅ Typing in st.text_input()
# ✅ Clicking st.button()
# ✅ Moving a st.slider()
# ✅ Changing a st.selectbox()
# ✅ Checking a st.checkbox()
# ✅ Selecting a radio button
# Typing in a text input → reruns the script, but st.button("Login") is False.
# Clicking the Login button → reruns the script, and st.button("Login") is True for that rerun only.

# Now when for the first time log in is done then
# by default navigation returns first page in list
# pg.run() runs that page.
# Now if user clicks another page from navigation then that click is 
# also considered a widget interaction and 
# the entire app script  reruns,recreates the page list 
# but this time navigation() remembers which page is clicked
# and pg.run() that page.
#if there is a button in any page, 
# the entire app reruns, and
# then Streamlit executes the currently selected page through pg.run().