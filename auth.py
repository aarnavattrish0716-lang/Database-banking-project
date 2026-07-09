from db import get_connection

def login(username,password):
    conn=get_connection();
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT user_id, user_name, role
    FROM users
    WHERE user_name=%s
    AND password=%s AND user_status=%s
    """
    cursor.execute(query,(username,password,"Active"))
    user=cursor.fetchone() ## fetched one row
    cursor.close()
    conn.close()
    return user # contains somethings like {"user_id":  ,"user_name":  ,"role": }


