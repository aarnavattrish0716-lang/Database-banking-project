import streamlit as st
import modules.admin_fun as md
import time

st.title("🏦 Account Management")

if st.session_state.role == "SUPER_ADMIN":
    st.info("Super Admin Mode")
else:
    st.info("Branch Head Mode")

# =====================================================
# Open New Account
# =====================================================

st.subheader("➕ Open New Account")

customers = md.get_customers()

with st.form("account_form", clear_on_submit=True):

    customer = st.selectbox(
        "Customer",
        options=customers,
        index=None,
        placeholder="Select Customer",
        format_func=lambda x:
            f"{x['user_id']} - {x['user_name']}"
    )

    account_type = st.selectbox(
        "Account Type",
        options=["SAVINGS", "CURRENT"],
        index=None,
        placeholder="Select Account Type"
    )

    initial_balance = st.number_input(
        "Initial Deposit",
        min_value=0.0,
        value=0.0,
        step=100.0
    )#Using this as streamlit automaticaaly validates it that it is >0.0 and user can type in this also

    branch_id = None

    if st.session_state.role == "SUPER_ADMIN":

        branches = md.get_active_branches()

        selected_branch = st.selectbox(
            "Branch",
            options=branches,
            index=None,
            placeholder="Select Branch",
            format_func=lambda x:
                f"{x['branch_name']} ({x['location']})"
        )

        if selected_branch:
            branch_id = selected_branch["branch_id"]

    else:

        branch_id = st.session_state.branch_id

        st.text_input(
            "Branch",
            value=st.session_state.branch_name,
            disabled=True
        )

    submit = st.form_submit_button("Open Account")

    if submit:

        if customer is None:
            st.warning("Please select a customer.")

        elif account_type is None:
            st.warning("Please select account type.")

        elif branch_id is None:
            st.warning("Please select a branch.")

        else:

            md.create_account(
                customer["user_id"],
                branch_id,
                account_type,
                initial_balance
            )

            time.sleep(2)
            st.rerun()

# =====================================================
# Existing Accounts
# =====================================================

st.divider()

st.subheader("📋 Existing Accounts")

if st.session_state.role == "SUPER_ADMIN":

    accounts = md.get_all_accounts()

else:

    accounts = md.get_branch_accounts(
        st.session_state.branch_id
    )

if accounts:

    st.dataframe(
        accounts,
        width="stretch",
        hide_index=True
    )

else:

    st.info("No accounts found.")

# =====================================================
# Freeze / Unfreeze Account
# =====================================================

st.divider()

st.subheader("🔄 Update Account Status")

if accounts:

    with st.form("account_status_form", clear_on_submit=True):

        selected_account = st.selectbox(
            "Account",
            options=accounts,
            index=None,
            placeholder="Select Account",
            format_func=lambda x:
                f"{x['account_id']} | "
                f"{x['user_name']} | "
                f"{x['branch_name']} | "
                f"{x['account_type']} | "
                f"{x['acc_status']}"
        )

        status = st.selectbox(
            "Status",
            options=["ACTIVE", "FROZEN"],
            index=None,
            placeholder="Select Status"
        )

        submit = st.form_submit_button("Update Status")

        if submit:

            if selected_account is None or status is None:

                st.warning("Please select all fields.")

            elif selected_account["acc_status"] == status:

                st.info("Account already has this status.")

            else:

                md.update_account_status(
                    selected_account["account_id"],
                    status
                )

                time.sleep(2)
                st.rerun()

else:

    st.info("No accounts available.")

# =====================================================
# Notes
# =====================================================

st.divider()

with st.expander("ℹ Rules"):

    st.markdown("""
- A customer can have multiple accounts.
- A customer cannot have two accounts of the same type in the same branch.
- Only active branches can open new accounts.
- Customer must have an ACTIVE login before opening an account.
- Branch Heads can only manage accounts belonging to their own branch.
- Super Admin can manage every account.
- Deactivating a customer freezes all of their accounts.
- Reactivating a customer does **not** automatically unfreeze accounts.
- Deactivating a branch freezes all accounts in that branch.
- Reactivating a branch does **not** automatically unfreeze accounts.
""")