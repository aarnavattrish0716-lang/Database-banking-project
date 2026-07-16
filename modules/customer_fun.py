import mysql.connector
import streamlit as st
from db import get_connection
def get_customer_dashboard(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        COUNT(account_id) AS Total_Accounts,
        SUM(acc_status='ACTIVE') AS Active_Accounts,
        COALESCE(
            SUM(
                CASE
                    WHEN acc_status='ACTIVE'
                    THEN balance
                    ELSE 0
                END
            ),
            0
        ) AS Total_Balance
    FROM customer_account_view
    WHERE user_id=%s
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data

def get_customer_loans(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        SUM(loan_status='APPROVED') AS Active_Loans,
        SUM(loan_status='PENDING') AS Pending_Loans
    FROM loans
    WHERE user_id=%s
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchone()

    if data["Active_Loans"] is None:
        data["Active_Loans"] = 0

    if data["Pending_Loans"] is None:
        data["Pending_Loans"] = 0

    cursor.close()
    conn.close()

    return data
def get_customer_accounts(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        account_id,
        branch_name,
        account_type,
        balance,
        acc_status
    FROM customer_account_view
    WHERE user_id=%s
    ORDER BY account_id
    """

    cursor.execute(query, (user_id,))

    accounts = cursor.fetchall()

    cursor.close()
    conn.close()

    return accounts

def get_customer_active_accounts(user_id):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT account_id,branch_name,account_type,balance FROM 
    customer_account_view
    WHERE user_id=%s AND acc_status='ACTIVE'
    ORDER BY account_id
    """
    cursor.execute(query,(user_id,))
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def transfer_customer_money(from_account, to_account, amount):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.callproc(
            "transfer_money",
            (
                from_account,
                to_account,
                amount
            )
        )

        conn.commit()

        st.success("Transfer completed successfully.")

    except mysql.connector.Error as e:

        conn.rollback()

        st.error(f"Database Error: {e.msg}")

    cursor.close()
    conn.close()
def get_customer_transactions(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        transaction_id,
        account_id,
        related_account_id,
        transaction_type,
        amount,
        transaction_date_time
    FROM customer_transactions_view
    WHERE user_id=%s
    ORDER BY transaction_date_time DESC
    """

    cursor.execute(query, (user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data