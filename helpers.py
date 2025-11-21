import random
import string


def generate_courier_data():
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for _ in range(10))
    password = ''.join(random.choice(letters) for _ in range(10))
    first_name = ''.join(random.choice(letters) for _ in range(10))
    return login, password, first_name

