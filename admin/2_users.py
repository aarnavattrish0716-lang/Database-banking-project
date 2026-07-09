import streamlit as st
import modules.admin_fun as md
import time
st.title("👥 User Management")
st.subheader("➕ Add User")
with st.form("user_form",clear_on_submit=True):
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    role = st.selectbox(label="Role",options=["ADMIN", "STAFF", "CUSTOMER"],placeholder="Select a role",index=None)
    submit_add=st.form_submit_button("Create User")
    if submit_add:
        if not username or not password or role is None:
            st.warning("Please fill the fields.")
        else:
            md.add_user(username,password,role)
            time.sleep(2)
            st.rerun()

st.divider()
st.subheader("📋 Existing Users")
users=md.get_all_users()
st.dataframe(users,use_container_width=True,hide_index=True)
st.subheader("🔄Change User Status")
with st.form("user_status_form",clear_on_submit=True):
    selected_user=st.selectbox(label="User",options=users,format_func=lambda x: f"{x['user_id']}-{x['user_name']}-{x['role']}-{x['user_status']}",placeholder="Select a User",index=None)
    status=st.selectbox(label="Status",options=["ACTIVE","INACTIVE"],placeholder="Select Status",index=None)
    submit_update=st.form_submit_button("Update Status")
    if submit_update:
        if selected_user is None or status is None:
            st.warning("Please select the fields.")
        else:
            md.update_user_status(selected_user['user_id'],status)
            time.sleep(2)
            st.rerun()
