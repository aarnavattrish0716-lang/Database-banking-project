import mysql.connector
import streamlit as st
from db import get_connection
## Function of home
def get_dashboard_counts():
    conn=get_connection()
    cursor=conn.cursor()
    counts={}
    cursor.execute("SELECT COUNT(*) FROM users")
    counts["users"]=cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM accounts")
    counts["accounts"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM branches")
    counts["branches"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM loans")
    counts["loans"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions")
    counts["transactions"] = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return counts
# fetchone retrieves the first row of the query result
# The result of query is actually like a record of table i.e row 
# if query returns rows then only first row is retrieved if 
# we save that in a variable then that variable is like a tuple ('Alice',25) or (15,) 
# so to get specific value we use []

## Functions of branch
def add_branch(branch_name,location):
    conn=get_connection()
    cursor=conn.cursor()
    query="Insert into branches (branch_name,location) values (%s,%s)"
    try:
        cursor.execute(query,(branch_name,location))
        conn.commit()
        st.success("Branch added successfully!")
    except mysql.connector.Error as e:
        st.error(f"Database Error:{e}")
    cursor.close()
    conn.close()
# Why use try and except:
# If suppose branch_name and location admin wants to insert already exists and there is a Unique(branch_name,location) constraint so database raises an error and our program 
# immediately crashes here rest of program does not execute.More such things that can happen like VAR(20) limit but user enter alot more program crashes

## mysql.connector.Error returns the exact error raised by database
# We use %s here not f-strings.Firstly %s here is not python string formatting but a placeholder,
# it is used in MySQL connector. 
# When we use f-string,Python first creates a big SQL string by replacing with the variables values and then
# it sends it to execute function, this can cause SQL-injection like branch_name = "Delhi'); DROP TABLE branches; --"
# location = "North" then Python first does INSERT INTO branches(branch_name, location)
# VALUES ('Delhi'); DROP TABLE branches; --', 'North') and then database recieves exactly this query causing our table to get deleted.
# When we use %s ,it sends query and data seperately,SQL receives query-INSERT INTO branches(branch_name, location)
# VALUES (?, ?) and data- Parameter 1:Delhi'); DROP TABLE branches; --Parameter 2:North so it knows that Delhi'); DROP TABLE branches; -- is a string.


# Why we used commit here because we are making changes in table the database doen't immediately make the changes permanent.
# Instead,it first records it in a transaction,when we do commit it makes the changes permanent.Most Python database libraries disable autocommit by default
# like here we have my.sql connector so we have to use commit,they do this because suppose autocommit is enabled ,if we have two query and one gets executed which withdraws money from one account
# it will get commited and other fails so it it will rollback till last commit,this is a problem money deducted but not added.
# Why this doesn't happen in workbench when we insert any thing it directly gets inserted ,because there by default autocommit is on.

def get_all_branch():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True) #By default the data returned by execute is in the form of tuple and to access each column seperated you have to remember that index 0 is id.. 
    query="SELECT * FROM branches ORDER BY branch_id"
    cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data #returns a list of dict
def update_branch_status(branch_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    query="""
            UPDATE branches
            SET branch_status = %s
            WHERE branch_id = %s
        """
    try:

        cursor.execute(query,(status, branch_id))
        conn.commit()
        st.success("Branch Status updated successfully!")
    except mysql.connector.Error as e:
        st.error(f"Database Error:{e}")
    cursor.close()
    conn.close()

## Functions of users
def add_user(username,password,role):
    conn=get_connection()
    cursor=conn.cursor()
    query="INSERT INTO USERS (user_name,password,role) VALUES(%s,%s,%s)"
    try:
        cursor.execute(query,(username,password,role))
        conn.commit()
        st.success("User added successfully!")
    except mysql.connector.Error as e:
        st.error(f"Database Error:{e}")
def get_all_users():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="SELECT * FROM USERS ORDER BY user_id"
    cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def update_user_status(user_id,status):
    conn = get_connection()
    cursor = conn.cursor()
    query="""
            UPDATE users
            SET user_status = %s
            WHERE user_id = %s
        """
    try:

        cursor.execute(query,(status, user_id))
        conn.commit()
        st.success("User Status updated successfully!")
    except mysql.connector.Error as e:
        st.error(f"Database Error:{e}")
    cursor.close()
    conn.close()

