import streamlit as st
import pandas as pd
import modules.customer_fun as md

st.title("📄 My Transactions")

transactions = md.get_customer_transactions(
    st.session_state.user_id
)

if not transactions:

    st.info("No transactions found.")

else:

    df = pd.DataFrame(transactions)

    df["transaction_date_time"] = pd.to_datetime(
        df["transaction_date_time"]
    )

    filtered = df.copy()

    st.subheader("🔍 Search / Filter")

    with st.container(border=True):

        col1, col2, col3 = st.columns(3)

        with col1:

            search_account = st.text_input(
                "Account ID"
            )

        with col2:

            search_type = st.selectbox(
                "Transaction Type",
                [
                    "ALL",
                    "DEPOSIT",
                    "WITHDRAW",
                    "TRANSFER"
                ]
            )

        with col3:

            search_date = st.date_input(
                "Transaction Date",
                value=None
            )

    if search_account:

        if search_account.isdigit():

            filtered = filtered[
                filtered["account_id"] == int(search_account)
            ]

        else:

            st.warning(
                "Account ID must be numeric."
            )

    if search_type != "ALL":

        filtered = filtered[
            filtered["transaction_type"] == search_type
        ]

    if search_date:

        filtered = filtered[
            filtered["transaction_date_time"].dt.date == search_date
        ]

    st.dataframe(
        filtered,
        hide_index=True,
        width="stretch"
    )