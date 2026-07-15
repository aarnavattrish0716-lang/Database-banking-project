import streamlit as st
import pandas as pd
import modules.admin_fun as md

st.title("📄 Transaction History")
df=pd.DataFrame(md.get_all_transactions())
df["transaction_date_time"]=pd.to_datetime(df['transaction_date_time'])
filtered=df.copy()
st.divider()
st.subheader("🔍 Search / Filter")
clear=st.button("🧹 Clear Filters")
if clear:
    st.session_state.search_name=""
    st.session_state.search_account_id=0
    st.session_state.search_transaction_type="ALL"
    st.session_state.search_date=None
with st.container(border=True):
    col1,col2,col3,col4=st.columns(4)
    with col1:
        search_name=st.text_input("Customer Name",key="search_name")
    if search_name:
        filtered=filtered[filtered["user_name"].str.lower().str.startswith(search_name.lower())]
    with col2:
        search_account_id=st.number_input("Account ID",min_value=0,key="search_account_id")
    if search_account_id!=0:
        filtered=filtered[filtered["account_id"]==search_account_id]
    with col3:
        options=["ALL","DEPOSIT","WITHDRAW","TRANSFER"]
        search_transaction_type=st.selectbox("Transaction Type",options=options,placeholder="All",key="search_transaction_type")
    if search_transaction_type!="ALL":
        filtered=filtered[filtered["transaction_type"]==search_transaction_type]
    with col4:
        search_date=st.date_input("Transaction Date",key="search_date",value=None) # default value current date
    if search_date:
        filtered=filtered[filtered["transaction_date_time"].dt.date==search_date]
st.dataframe(filtered,width="stretch",hide_index=True)
# If i want to clear the inputs of all widgets then i would need to attach a key with them 
# and then reset the corresponding st.session_state values.Key name should be unique may or may not be equal to widget name.
# If i try to do search_name="" then it will not reset the widget to "" it only changes python variable text box still shows same value
