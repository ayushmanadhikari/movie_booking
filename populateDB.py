#establishing a database connection
from mysql.connector import connect, Error, cursor
from faker import Faker
import random

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
    print("connection established!!!")
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

#user table
id_range = range(1, 50)
#popultaing user table
def generate_user_data():
    i = 0
    while i < 10:
        fake = Faker()
        u_id = random.choice(id_range)
        u_name = fake.name()
        email = fake.email()
        location = fake.address()
        user_insert_query = f"INSERT INTO user (u_id, u_name, email, location) VALUES ({u_id}, '{u_name}', '{email}', '{location}');"
        try: 
            myCursor.execute(user_insert_query)
            mydb.commit()
        except Error as e:
            print(e)
        i += 10


def generate_movie_data():
    

    return 1



generate_user_data()

#for x in myResult:
#    print(x)




