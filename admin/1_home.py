import streamlit as st

st.title("🏦 Admin Dashboard")

st.write(f"Welcome {st.session_state.username}")

if st.button("Logout"):
    st.session_state.logged_in=False
    st.rerun()

## st.rerun restarts the streamlit app from its entry script i.e app.py if navigation() was used in app.py and rerun() is used in any of the navigation.
## If instead of navigation() ,pages/ was used which automatically creates pages and if i click any page that page runs if i do rerun() in that page then only page will rerun not entire script