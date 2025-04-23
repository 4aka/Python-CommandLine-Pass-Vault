from Assertions import is_password_file_exists
from PasswordActions import (compare_password_with_existed, create_password, input_data)
from Assertions import passwords_equels
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
    password = input_data('New password: ')
    assert_password = input_data('New password again: ')
    while not passwords_equels(password, assert_password):
        print('Passwords do not match! Try again')
        password = input_data('New password: ')
        assert_password = input_data('New password again: ')

    # TODO check input for cirylyc
    create_password(password)
    create_vault()


def existed_user_scenario():
    password = input('Password: ')
    # password has to be hashed
    while not compare_password_with_existed(hash_data(password)):
        print('Wrong password! Try again')
        password = input('Password: ')
    # TODO check vault


def create_vault():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()


def get_bool(prompt):
    while True:
        try:
            return {"y": True, "n": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input please enter y or n!")


def copy_to_clipboard(data):
    pyperclip.copy(data)
