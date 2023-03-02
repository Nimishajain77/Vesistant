import mysql.connector as sql_conn

# mydb = sql_conn.connect(
#     host="localhost",
#     user="root",
#     password=""
# )

# print(mydb)



mydb = sql_conn.connect(
    host="localhost",
    user="root",
    password="",
    database="face_rec"
)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE face_rec")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

cursor = mydb.cursor()
cursor.execute(
   "create table user_table(id int primary key, Name varchar(50), Password varchar(50), Email varchar(50))")

cursor.execute("SHOW TABLES")
for x in cursor:
   print(x)
