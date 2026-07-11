import streamlit as st
import time
import modules.admin_fun as md
if st.session_state.role!="SUPER_ADMIN":
    st.error("Access Denied")
    st.stop()
st.title("🏦 Branch Management")
st.subheader("➕ Add Branch")
with st.form("branch_form",clear_on_submit=True):
    branch_name=st.text_input("Branch Name")
    location=st.text_input("Location")
    submit_add=st.form_submit_button("Add branch")
    if submit_add:
        if not branch_name or not location:
            st.warning("Please fill the fields.")
        else:
            md.add_branch(branch_name,location)
            time.sleep(2)
            st.rerun()
st.divider()          
st.subheader("🏦 Existing Branches")
branches=md.get_all_branch()
if branches:
    st.dataframe(branches,width='stretch',hide_index=True)
else:
    st.info("🏦 No branches found. Add your first branch to get started.")
st.subheader("🔄Update Branch Status")
if branches: # If branches is empty it will return [] and it is treated as false
    with st.form("Update Branch Status",clear_on_submit=True):
        selected=st.selectbox(label="Branch",options=branches,format_func=lambda x: f"{x['branch_name']}-{x['location']}-{x['branch_status']}",placeholder="Choose a branch",index=None)
        status=st.selectbox(label="Status",options=["ACTIVE","INACTIVE"],placeholder="Select Status",index=None)
        submit_update=st.form_submit_button("Update Status")
        if submit_update:
            if selected is None or status is None:
                st.warning("Please select the fields.")
            else:
                md.update_branch_status(selected['branch_id'],status)
                time.sleep(2)
                st.rerun()
else:
    st.info("🏦 No branches found. Add your first branch to get started.")
# We are using with here because otherwise we have to mention which form these text_input belongs to
# form = st.form("branch_form")
# branch_name = form.text_input("Branch Name")
# location = form.text_input("Location")
# submit = form.form_submit_button("Add Branch")


