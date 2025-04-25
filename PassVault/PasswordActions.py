from Tools import hash_data
from Variables import passowrd_file


def create_password(password):
    hashed_password = hash_data(password)
    f = open(passowrd_file, "w")
    f.write(hashed_password)
    f.close()


def compare_password_with_existed(password):
    return read_password() == password


def read_password():
    f = open(passowrd_file, "r")
    password = f.read()
    f.close()
    return password


def read_password_bytes():
    f = open(passowrd_file, "rb")
    password = f.read()
    f.close()
    return password
