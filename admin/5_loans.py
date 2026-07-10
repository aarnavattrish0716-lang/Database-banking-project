import streamlit as st
import modules.admin_fun as md 
import time
st.title("Loan Management")
st.subheader("📋Loan Applications")
loan_details=md.get_all_loans()
st.dataframe(loan_details,width="stretch",hide_index=True)
if st.session_state.role=="SUPER_ADMIN":
    st.divider()
    st.subheader("🔄Review Pending Loan Applications")
    pending_loans=md.get_pending_loans()
    if pending_loans:
        with st.form("loan_status_form",clear_on_submit=True):
            selected_loan=st.selectbox(label="Select loan",options=pending_loans,format_func=lambda x:f"{x['loan_id']}-{x['user_name']}-{x['loan_type']}-{x['amount']}",placeholder="Choose a pending loan",index=None)
            selected_status=st.selectbox(label="Status",options=["APPROVED","REJECTED"],placeholder="Select loan status",index=None)
            submit=st.form_submit_button("Update Status")
        if submit:
            if selected_loan is None or selected_status is None:
                st.warning("Please select the fields.")
            else:
                md.update_loan_status(selected_loan["loan_id"],selected_status)
                time.sleep(2)
                st.rerun()
    else:
        st.info("There are no pending loan applications.")