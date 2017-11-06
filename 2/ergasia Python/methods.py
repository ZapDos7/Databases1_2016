import pymysql
import settings

def connection():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema)

    return conn

def insertData():
    con=connection()
    cur=con.cursor()
    cur.execute("") #pending
    cur.commit()
    
    return [("status",),("ok!")]

def retriveData():
    con=connection()
    cur=con.cursor()
    cur.execute("") #pending
    cur.commit()
    
    return [("status",),("ok!")]

conn=pymysql.connect(
    settings.mysql_host,
    settings.mysql_user,
    settings.mysql_passwd,
    settings.mysql_schema)
cur=conn.cursor()
cur.execute("SELECT epitheto FROM kalitexnis")
print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()
