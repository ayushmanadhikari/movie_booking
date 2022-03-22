#establishing a database connection
from django.db import connection
from mysql.connector import connect, Error, cursor


CONS_HOST = "localhost"
CONS_USER = "root"
CONS_PASS = ""


#connecting with database
try:
    mydb = connect(
        host=CONS_HOST,
        user=CONS_USER,
        password=CONS_PASS,
    ) 
    print(mydb)
except Error as e:
    print(e)


#checking the available databases, tables
show_db_query = "show databases;"
select_db_query = "use booking_pro;"
show_table_query = "show tables;"

myCursor = mydb.cursor()
myCursor.execute(select_db_query)
myCursor.execute(show_table_query)
myResult = myCursor.fetchall()

for x in myResult:
    print(x)



