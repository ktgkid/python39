import pymysql

host = 'localhost'
port = 3356
db = 'bigdata'
user = 'root'
passwd = 'love1004'
charset = 'utf8'

conn = None
cur = None

def openConn():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
    cur = conn.cursor()
    return cur

def closeConn():
    cur.close()
    conn.close()