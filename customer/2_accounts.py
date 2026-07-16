import streamlit as st
import pandas as pd
import modules.customer_fun as md

st.title("🏦 My Accounts")

accounts = md.get_customer_accounts(
    st.session_state.user_id
)

if not accounts:

    st.warning(
        "No accounts have been assigned to you yet."
    )

else:

    df = pd.DataFrame(accounts)

    st.dataframe(
        df,
        hide_index=True,
        width="stretch"
    )

   

    