import mysql.connector
import streamlit as st
from db import get_connection

def get_staff_dashboard(branch_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT

        (
            SELECT COUNT(DISTINCT a.user_id)
            FROM accounts a
            WHERE a.branch_id=%s
        ) AS customers,

        (
            SELECT COUNT(*)
            FROM accounts
            WHERE branch_id=%s
        ) AS accounts,

        (
            SELECT COUNT(*)
            FROM transactions t
            JOIN accounts a
                ON t.account_id=a.account_id
            WHERE a.branch_id=%s
        ) AS transactions
    """

    cursor.execute(
        query,
        (
            branch_id,
            branch_id,
            branch_id
        )
    )

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data

def get_active_branch_accounts(branch_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        a.account_id,
        u.user_name,
        a.account_type,
        a.balance
    FROM accounts a

    JOIN users u
        ON a.user_id = u.user_id

    WHERE
        a.branch_id=%s
        AND a.acc_status='ACTIVE'

    ORDER BY
        a.account_id
    """

    cursor.execute(query, (branch_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def staff_deposit(account_id, amount):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.callproc(
            "deposit_money",
            (
                account_id,
                amount
            )
        )

        conn.commit()

        st.success(
            "Deposit successful."
        )

    except mysql.connector.Error as e:

        conn.rollback()

        st.error(e.msg)

    cursor.close()
    conn.close()
def staff_withdraw(account_id, amount):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.callproc(
            "withdraw_money",
            (
                account_id,
                amount
            )
        )

        conn.commit()

        st.success(
            "Withdrawal successful."
        )

    except mysql.connector.Error as e:

        conn.rollback()

        st.error(e.msg)

    cursor.close()
    conn.close()

def staff_transfer(from_account, to_account, amount):

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

        st.success(
            "Transfer completed successfully."
        )

    except mysql.connector.Error as e:

        conn.rollback()

        st.error(e.msg)

    cursor.close()
    conn.close()