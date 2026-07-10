import streamlit as st
import modules.admin_fun as md
import time
st.title("👥 User Management")
if st.session_state.role == "SUPER_ADMIN":
    st.info("Super Admin Mode")
else:
    st.info("Branch Head Mode")
st.subheader("➕ Add User")
if st.session_state.role == "SUPER_ADMIN":
    options = ["BRANCH_HEAD", "STAFF", "CUSTOMER"]
else:
    options = ["STAFF", "CUSTOMER"]
role = st.selectbox(
    "Role",
    options,
    index=None,
    placeholder="Select Role"
)
with st.form("user_form",clear_on_submit=True):
    username=st.text_input("Username")
    password=st.text_input("Password",type="password")
    branch_id = None
    if role == "BRANCH_HEAD":
        branches = md.get_active_branches()
        selected_branch = st.selectbox(
            "Branch",
            options=branches,
            format_func=lambda x: f"{x['branch_name']} ({x['location']})",
            index=None,
         placeholder="Select Branch"
        )
        if selected_branch:
             branch_id = selected_branch["branch_id"]

    elif role == "STAFF":
        if st.session_state.role == "SUPER_ADMIN":
            branches = md.get_active_branches()

            selected_branch = st.selectbox(
                "Branch",
                options=branches,
                format_func=lambda x: f"{x['branch_name']} ({x['location']})",
                index=None,
                placeholder="Select Branch"
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
    submit_add=st.form_submit_button("Create User")
    if submit_add:
        if not username or not password or role is None:
            st.warning("Please fill the fields.")
        elif role in ["BRANCH_HEAD", "STAFF"] and branch_id is None:
            st.warning("Please select a branch.")   
        else:
            md.add_user(username,password,role,branch_id)
            time.sleep(2)
            st.rerun()

st.divider()
st.subheader("📋 Existing Users")
if st.session_state.role == "SUPER_ADMIN":

    users = md.get_all_users()

else:
    users = md.get_branch_staff(
        st.session_state.branch_id
    )
st.dataframe(users,width='stretch',hide_index=True)
st.divider()
st.subheader("🔄Change User Status")
if st.session_state.role == "SUPER_ADMIN":
    users = md.get_manageable_users(
        "SUPER_ADMIN",
        None
    )
else:
    users = md.get_manageable_users(
        "BRANCH_HEAD",
        st.session_state.branch_id
    )
with st.form("user_status_form",clear_on_submit=True):
    selected_user=st.selectbox(label="User",options=users,format_func=lambda x: f"{x['user_id']}-{x['user_name']}-{x['role']}-{x['user_status']}",placeholder="Select a User",index=None)
    status=st.selectbox(label="Status",options=["ACTIVE","INACTIVE"],placeholder="Select Status",index=None)
    submit_update=st.form_submit_button("Update Status")
    if submit_update:
        if selected_user is None or status is None:
            st.warning("Please select the fields.")
        elif selected_user["role"] == "SUPER_ADMIN":
            st.error("Super Admin account cannot be deactivated.")
        else:
            md.update_user_status(
                selected_user["user_id"],
                status
            )
            time.sleep(2)
            st.rerun()