import streamlit as st
import modules.staff_fun as md
import time

st.title("🔁 Transfer Money")

accounts = md.get_active_branch_accounts(
    st.session_state.branch_id
)

if not accounts:

    st.info("No active accounts available.")

else:

    with st.form(
        "staff_transfer_form",
        clear_on_submit=True
    ):

        from_account = st.selectbox(
            "From Account",
            options=accounts,
            index=None,
            placeholder="Select Account",
            format_func=lambda x:
                f"{x['account_id']} | "
                f"{x['user_name']} | "
                f"{x['account_type']} | "
                f"₹{x['balance']:.2f}"
        )

        to_account = st.text_input(
            "Receiver Account ID",
            placeholder="Enter receiver account ID"
        )

        amount = st.number_input(
            "Amount",
            min_value=0.01,
            step=100.0
        )

        submit = st.form_submit_button(
            "Transfer"
        )

        if submit:

            if from_account is None:

                st.warning(
                    "Please select a sender account."
                )

            elif not to_account:

                st.warning(
                    "Please enter the receiver account ID."
                )

            elif not to_account.isdigit():

                st.warning(
                    "Receiver Account ID must be numeric."
                )

            else:

                md.staff_transfer(
                    from_account["account_id"],
                    int(to_account),
                    amount
                )

                time.sleep(2)

                st.rerun()