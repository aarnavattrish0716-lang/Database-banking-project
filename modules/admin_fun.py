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

    try:

        cursor.execute(
            """
            UPDATE branches
            SET branch_status = %s
            WHERE branch_id = %s
            """,
            (status, branch_id)
        )
        if status == "INACTIVE":

            cursor.execute(
                """
                UPDATE users
                SET user_status = 'INACTIVE'
                WHERE branch_id = %s
                """,
                (branch_id,)
            )

            cursor.execute(
                """
                UPDATE accounts
                SET acc_status = 'FROZEN'
                WHERE branch_id = %s
                """,
                (branch_id,)
            )

        conn.commit()

        st.success("Branch status updated successfully!")

    except mysql.connector.Error as e:
        conn.rollback()
        st.error(f"Database Error: {e}")
    cursor.close()
    conn.close()

## Functions of users
def add_user(username, password, role, branch_id):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        if role == "BRANCH_HEAD":

            cursor.execute(
                """
                SELECT user_id
                FROM users
                WHERE role = 'BRANCH_HEAD'
                  AND branch_id = %s
                  AND user_status="ACTIVE"
                """,
                (branch_id,)
            )

            if cursor.fetchone():
                st.error("This branch already has a Branch Head.")
                return

        query = """
        INSERT INTO users
        (user_name, password, role, branch_id)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (username, password, role, branch_id)
        )

        conn.commit()

        st.success("User added successfully!")

    except mysql.connector.Error as e:
        st.error(f"Database Error: {e}")
        
    cursor.close()
    conn.close()
    
def get_all_users():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        u.user_id,
        u.user_name,
        u.role,
        b.branch_name,
        u.user_status
    FROM users u
    LEFT JOIN branches b
        ON u.branch_id = b.branch_id
    ORDER BY
        u.role,
        u.user_id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def get_branch_staff(branch_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT
        u.user_id,
        u.user_name,
        u.role,
        b.branch_name,
        u.user_status
    FROM users u
    JOIN branches b
        ON u.branch_id = b.branch_id
    WHERE
        u.role='STAFF'
        AND u.branch_id=%s
    ORDER BY
        u.user_id
    """
    cursor.execute(query, (branch_id,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def get_manageable_users(role, branch_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if role == "SUPER_ADMIN":

        query = """
        SELECT
            user_id,
            user_name,
            role,
            user_status,
            branch_id
        FROM users
        WHERE role IN
        (
            'BRANCH_HEAD',
            'STAFF',
            'CUSTOMER'
        )
        ORDER BY
            role,
            user_id
        """

        cursor.execute(query)

    else:

        query = """
        SELECT
            user_id,
            user_name,
            role,
            user_status,
            branch_id
        FROM users
        WHERE
            role='STAFF'
            AND branch_id=%s
        ORDER BY
            user_id
        """

        cursor.execute(query, (branch_id,))

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def update_user_status(user_id, role, branch_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        if role == "BRANCH_HEAD" and status == "ACTIVE":

            cursor.execute(
                """
                SELECT user_id
                FROM users
                WHERE
                    role = 'BRANCH_HEAD'
                    AND branch_id = %s
                    AND user_status = 'ACTIVE'
                    AND user_id != %s
                """,
                (branch_id, user_id)
            )

            if cursor.fetchone():

                st.error(
                    "This branch already has an active Branch Head."
                )
                return

        cursor.execute(
            """
            UPDATE users
            SET user_status = %s
            WHERE user_id = %s
            """,
            (status, user_id)
        )
        if role == "CUSTOMER" and status == "INACTIVE":

            cursor.execute(
                """
                UPDATE accounts
                SET acc_status = 'FROZEN'
                WHERE user_id = %s
                """,
                (user_id,)
            )

        conn.commit()

        st.success("User status updated successfully!")

    except mysql.connector.Error as e:

        conn.rollback()

        st.error(f"Database Error: {e}")

    finally:

        cursor.close()
        conn.close()
def get_active_branches():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM branches
    WHERE branch_status='ACTIVE'
    ORDER BY branch_name
    """

    cursor.execute(query)

    branches = cursor.fetchall()

    cursor.close()
    conn.close()

    return branches

def get_customers():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        user_id,
        user_name
    FROM users
    WHERE
        role='CUSTOMER'
        AND user_status="ACTIVE"
    ORDER BY user_name
    """

    cursor.execute(query)

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return customers
def create_account(user_id, branch_id, account_type, initial_balance):

    conn = get_connection()
    cursor = conn.cursor()

    try:


        cursor.execute(
            """
            SELECT user_status
            FROM users
            WHERE user_id=%s
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if row is None:
            st.error("Customer not found.")
            return

        if row[0] != "ACTIVE":
            st.error("Customer login is inactive.")
            return

        cursor.execute(
            """
            SELECT branch_status
            FROM branches
            WHERE branch_id=%s
            """,
            (branch_id,)
        )

        row = cursor.fetchone()

        if row[0] != "ACTIVE":
            st.error("Branch is inactive.")
            return


        cursor.execute(
            """
            SELECT account_id
            FROM accounts
            WHERE
                user_id=%s
                AND branch_id=%s
                AND account_type=%s
            """,
            (
                user_id,
                branch_id,
                account_type
            )
        )

        if cursor.fetchone():

            st.error(
                "Customer already has this account type in this branch."
            )

            return

        cursor.execute(
            """
            INSERT INTO accounts
            (
                user_id,
                branch_id,
                account_type,
                balance
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                user_id,
                branch_id,
                account_type,
                initial_balance
            )
        )
                                      # database automatically generated account_id as it has autoincrement constraint 
                                      # Immediately after an INSERT, the connector remembers the value generated by the database.
        account_id = cursor.lastrowid #It simply returns the auto-generated primary key from the most recent INSERT executed by that cursor

        if initial_balance > 0:

            cursor.execute(
                """
                INSERT INTO transactions
                (
                    account_id,
                    transaction_type,
                    amount
                )
                VALUES
                (
                    %s,
                    'DEPOSIT',
                    %s
                )
                """,
                (
                    account_id,
                    initial_balance
                )
            )

        conn.commit()

        st.success("Account created successfully.")

    except mysql.connector.Error as e:

        conn.rollback()

        st.error(f"Database Error : {e}")

    cursor.close()
    conn.close()
def get_all_accounts():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT

        a.account_id,

        u.user_name,
        
        u.user_status,

        b.branch_name,

        a.account_type,

        a.balance,

        a.acc_status

    FROM accounts a

    JOIN users u
        ON a.user_id=u.user_id

    JOIN branches b
        ON a.branch_id=b.branch_id

    ORDER BY
        a.account_id
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()

    conn.close()

    return data
def get_branch_accounts(branch_id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT

        a.account_id,

        u.user_name,

        u.user_status,

        b.branch_name,

        a.account_type,

        a.balance,

        a.acc_status

    FROM accounts a

    JOIN users u
        ON a.user_id=u.user_id

    JOIN branches b
        ON a.branch_id=b.branch_id

    WHERE
        a.branch_id=%s

    ORDER BY
        a.account_id
    """

    cursor.execute(
        query,
        (branch_id,)
    )

    data = cursor.fetchall()

    cursor.close()

    conn.close()

    return data
def get_manageable_accounts(role, branch_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if role == "SUPER_ADMIN":

        query = """
        SELECT
            a.account_id,
            u.user_name,
            b.branch_name,
            a.account_type,
            a.balance,
            a.acc_status
        FROM accounts a

        JOIN users u
            ON a.user_id = u.user_id

        JOIN branches b
            ON a.branch_id = b.branch_id

        WHERE
            u.user_status = 'ACTIVE'

        ORDER BY
            a.account_id
        """

        cursor.execute(query)

    else:

        query = """
        SELECT
            a.account_id,
            a.user_id,
            u.user_name,
            b.branch_name,
            a.account_type,
            a.balance,
            a.acc_status
        FROM accounts a

        JOIN users u
            ON a.user_id = u.user_id

        JOIN branches b
            ON a.branch_id = b.branch_id

        WHERE
            u.user_status = 'ACTIVE'
            AND a.branch_id = %s

        ORDER BY
            a.account_id
        """

        cursor.execute(query, (branch_id,))

    accounts = cursor.fetchall()

    cursor.close()
    conn.close()

    return accounts
def update_account_status(account_id, status):

    conn = get_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            UPDATE accounts
            SET acc_status=%s
            WHERE account_id=%s
            """,
            (
                status,
                account_id
            )
        )

        conn.commit()

        st.success(
            "Account status updated successfully."
        )

    except mysql.connector.Error as e:

        st.error(
            f"Database Error : {e}"
        )

    cursor.close()

    conn.close()
def get_all_loans():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT l.loan_id,u.user_name,u.user_status,
    l.loan_type,l.amount,l.loan_status
    FROM loans as l JOIN
    users as u on
    u.user_id=l.user_id
    """ 
    cursor.execute(query)
    data=cursor.fetchall()    
    cursor.close()
    conn.close()
    return data
def get_pending_loans():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT l.loan_id,u.user_name,
    l.loan_type,l.amount,l.loan_status
    FROM loans l JOIN
    users u ON
    l.user_id=u.user_id
    WHERE u.user_status=%s
    AND l.loan_status=%s
    """
    cursor.execute(query,("ACTIVE","PENDING"))
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def update_loan_status(loan_id,loan_status):
    conn=get_connection()
    cursor=conn.cursor()
    try:
        query="""
        UPDATE loans
        SET loan_status=%s
        WHERE loan_id=%s
        """
        cursor.execute(query,(loan_status,loan_id))
        conn.commit()
        st.success("Loan Status Updated")
    except mysql.connector.Error as e:
        st.error(f"Database Error:{e}")
    cursor.close()
    conn.close()
def get_all_transactions():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    if st.session_state.role=="SUPER_ADMIN":
        query="""
        SELECT
        t.transaction_id,
        u.user_name,
        a.account_id,
        b.branch_name,
        t.transaction_type,
        t.amount,
        t.transaction_date_time
        FROM transactions t

        JOIN accounts a
        ON t.account_id = a.account_id

        JOIN users u
        ON a.user_id = u.user_id

        JOIN branches b
        ON a.branch_id = b.branch_id

        ORDER BY
        t.transaction_date_time DESC;
        """
        cursor.execute(query)
    else:
        query="""
             SELECT
            t.transaction_id,
            u.user_name,
            a.account_id,
            b.branch_name,
            t.transaction_type,
            t.amount,
            t.transaction_date_time
        FROM transactions t
        JOIN accounts a
        ON t.account_id = a.account_id
        JOIN users u
        ON a.user_id = u.user_id
        JOIN branches b
        ON a.branch_id = b.branch_id
        WHERE
        a.branch_id=%s
        ORDER BY
        t.transaction_date_time DESC;
    """
        cursor.execute(query,(st.session_state.branch_id,))
    data=cursor.fetchall() 
    cursor.close()
    conn.close()
    return data