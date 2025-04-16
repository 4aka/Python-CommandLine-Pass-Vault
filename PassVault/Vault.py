from Assertions import is_password_file_exists
from PasswordActions import (compare_passwords, compare_password_with_existed,
                             create_password, read_db_password, create_db_password)
from cryptography.fernet import Fernet
from Variables import vault_file, create_table_sql
from HashData import hash_data
import sqlite3
import pyperclip


def login():
    if is_password_file_exists():
        existed_user_scenario()
    else:
        new_user_scenario()


def new_user_scenario():
    new_password = input('New password: ')
    assert_password = input('New password again: ')
    while not compare_passwords(new_password, assert_password):
        print('Passwords do not match! Try again')
        new_password = input('New password: ')
        assert_password = input('New password again: ')

    create_password(new_password)
    create_db_password()
    create_vault()


def existed_user_scenario():
    password = input('Password: ')
    # password has to be hashed
    while not compare_password_with_existed(hash_data(password)):
        print('Wrong password! Try again')
        password = input('Password: ')


def create_vault():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()


def decrypt(encrypted_password):
    key = read_db_password()
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()


def encrypt(data):
    key = read_db_password()
    f = Fernet(key)
    return f.encrypt(data)


def get_bool(prompt):
    while True:
        try:
            return {"y": True, "n": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input please enter True or False!")


def copy_to_clipboard(data):
    pyperclip.copy(data)
