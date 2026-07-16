import streamlit as st
import  modules.admin_fun as md
from datetime import datetime 
now = datetime.now()
## here markdown see a string and it sends it to browser,browser receives HTML and CSS which it parse and draws the layout
st.markdown(f"""
<div style="
padding:20px;
border-radius:15px;
background:rgba(255,255,255,0.05);
border:1px solid #444;
">
<h2>👋 Welcome back , {st.session_state.username}</h2>
<p style="font-size:18px;">📅 {now.strftime('%A, %d %B %Y')}</p>
<p style="font-size:18px;">🕒 {now.strftime('%I:%M %p')}</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.role == "SUPER_ADMIN":
    counts = md.get_dashboard_counts()
else:
    counts = md.get_branch_dashboard_counts(
        st.session_state.branch_id
    )
with st.container(border=True,height="content",horizontal=True):
    if st.session_state.role=="SUPER_ADMIN":
        col1, col2, col3, col4, col5= st.columns(5)

        with col1:
            with st.container(border=True):
                st.metric(label="👥 Users",value=counts["users"])

        with col2:
            with st.container(border=True): 
                st.metric(label="💳 Accounts",value=counts["accounts"])

        with col3:
            with st.container(border=True): 
                st.metric(label="🏢 Branches",value=counts["branches"])

        with col4:
            with st.container(border=True): 
                st.metric(label="💰 Loans",value=counts["loans"])

        with col5:
            with st.container(border=True):  
                st.metric(label="🔄 Transactions",value=counts["transactions"])
    else:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            with st.container(border=True): 
                st.metric("👨‍💼 Staff", counts["users"])

        with col2:
            with st.container(border=True): 
                st.metric("💳 Accounts", counts["accounts"])

        with col3:
            with st.container(border=True): 
                st.metric("💰 Loans", counts["loans"])

        with col4:
            with st.container(border=True): 
                st.metric("🔄 Transactions", counts["transactions"])
if st.button("Logout"):
    st.session_state.logged_in=False
    st.rerun()

## st.rerun restarts the streamlit app from its entry script i.e app.py if navigation() was used in app.py and rerun() is used in any of the navigation.
## If instead of navigation() ,pages/ was used which automatically creates pages and if i click any page that page runs if i do rerun() in that page then only page will rerun not entire script