import random 
from faker import Faker



id_list = range(0,20)
def generate_data():
    fake = Faker()
    u_name = fake.name()
    email = fake.email()
    location = fake.address()
    id = random.choice(id_list)
    print(id,u_name, email, location)

m_name = "heman" * 5
print(m_name)