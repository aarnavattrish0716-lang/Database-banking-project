import streamlit as st
import modules.customer_fun as md
import time
st.title("🔁 Transfer Money")
accounts=md.get_customer_active_accounts(st.session_state.user_id)
if not accounts:
    st.warning("You do not have any active accounts.")
else:
    with st.form("transfer_form",clear_on_submit=True):
    
        from_account=st.selectbox("From Account",options=accounts,index=None,placeholder="Select the Source account",format_func=lambda x:f"{x["account_id"]}-{x['branch_name']}-{x['account_type']}-₹{x['balance']:.2f}")
        to_account=st.text_input("Receiver Account ID",placeholder="Enter receiver account ID") # Not using number_input because we want default value to be None
        amount = st.number_input(
            "Amount",
            min_value=0.01,
            step=1.0
        )

        submit=st.form_submit_button("Transfer")
        if submit:
            if from_account is None:

                st.warning(
                    "Please select a source account."
                )
            elif not to_account:
                st.warning("Please enter the receiver account ID.")

            elif not to_account.isdigit():
                st.warning("Receiver Account ID must be a positive integer.")
            else:

                md.transfer_customer_money(
                    from_account["account_id"],
                    int(to_account),
                    amount
                )
                time.sleep(2)
                st.rerun()
