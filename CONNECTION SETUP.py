import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",passwd="India@2022")
cursor=mydb.cursor()
cursor.execute("show databases;")
print(cursor.fetchall())