import mysql.connector
import streamlit as st
from db import get_connection

def get_customer_dashboard(user_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query = """
SELECT
    COUNT(account_id) AS Total_Accounts,
    SUM(balance) AS Total_Balance
FROM customer_account_view
WHERE user_id=%s
"""
    cursor.execute(query,(user_id,))
    data=cursor.fetchone()
    cursor.close()
    conn.close()
    return data

def get_customer_loans(user_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query = """
    SELECT COUNT(*) AS Total_Loans
FROM loans
WHERE user_id=%s
"""
    cursor.execute(query,(user_id,))
    data=cursor.fetchone()
    cursor.close()
    conn.close()
    return data