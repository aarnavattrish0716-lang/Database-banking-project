from db import get_connection

def login(username,password):
    conn=get_connection();
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT
    u.user_id,
    u.user_name,
    u.role,
    u.branch_id,
    b.branch_name
    FROM users u
    LEFT JOIN branches b
    ON u.branch_id=b.branch_id
    WHERE user_name=%s
    AND password=%s AND user_status=%s
    """
    cursor.execute(query,(username,password,"Active"))
    user=cursor.fetchone() ## fetched one row
    cursor.close()
    conn.close()
    return user # contains somethings like {"user_id":  ,"user_name":  ,"role": }


