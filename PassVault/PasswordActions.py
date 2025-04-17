from cryptography.fernet import Fernet

from HashData import hash_data
from Variables import passowrd_file, passowrd_db_file
import base64


def create_password(password):
    hashed_password = hash_data(password)
    f = open(passowrd_file, "w")
    f.write(hashed_password)
    f.close()


def create_db_password():
    f = open(passowrd_db_file, "wb")
    key = Fernet.generate_key()
    base_key = base64.b64encode(key)
    f.write(base_key)
    f.close()


def read_db_password():
    f = open(passowrd_db_file, "rb")
    bytes_file = f.read()
    password = base64.b64decode(bytes_file)
    f.close()
    return password


def compare_password_with_existed(password):
    existed_password = read_password()
    return existed_password == password


def compare_passwords(password_1, password_2):
    return password_1 == password_2


def read_password():
    f = open(passowrd_file, "r")
    password = f.read()
    f.close()
    return password


def input_password(input_text):
    return input(input_text)

