#establishing a database connection
from getpass import getpass
from django.db import connection
from mysql.connector import connect, Error


CONS_HOST = "localhost"
CONS_USER = "root"
CONS_PASS = ""


try:
    mydb = connect(
        host=CONS_HOST,
        user=CONS_USER,
        password=CONS_PASS,
    ) 
    print(mydb)
except Error as e:
    print(e)


