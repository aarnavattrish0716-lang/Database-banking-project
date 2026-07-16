import streamlit as st
import modules.staff_fun as md
import time

st.title("💵 Deposit Money")

accounts = md.get_active_branch_accounts(
    st.session_state.branch_id
)

if not accounts:

    st.info(
        "No active accounts found."
    )

else:

    with st.form(
        "deposit_form",
        clear_on_submit=True
    ):

        account = st.selectbox(
            "Account",
            options=accounts,
            index=None,
            placeholder="Select Account",
            format_func=lambda x:
                f"{x['account_id']} | "
                f"{x['user_name']} | "
                f"{x['account_type']} | "
                f"₹{x['balance']:.2f}"
        )

        amount = st.number_input(
            "Amount",
            min_value=0.01,
            step=100.0
        )

        submit = st.form_submit_button(
            "Deposit"
        )

        if submit:

            if account is None:

                st.warning(
                    "Please select an account."
                )

            else:

                md.staff_deposit(
                    account["account_id"],
                    amount
                )

                time.sleep(2)

                st.rerun()