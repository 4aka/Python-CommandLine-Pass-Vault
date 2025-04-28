from Assertions import is_password_file_exists, is_vault_file_exists
from Tools import get_bool, hash_data
from PasswordActions import compare_password_with_existed, create_password
from Assertions import passwords_equels, assert_input
from Variables import vault_file, create_table_sql
import sqlite3


def login():
    if is_password_file_exists():
        existed_user_scenario()
    else:
        new_user_scenario()


def new_user_scenario():
    password = assert_input('\nCreate password: ')
    assert_password = assert_input('Confirm password: ')

    while not passwords_equels(password, assert_password):
        print('Passwords do not match! Try again')
        password = assert_input('\nCreate password: ')
        assert_password = assert_input('Confirm password: ')

    create_password(password)
    create_vault()


def existed_user_scenario():
    password = assert_input('\nPassword: ')

    while not compare_password_with_existed(hash_data(password)):
        print('Wrong password! Try again')
        password = assert_input('\nPassword: ')
    if not is_vault_file_exists():
        ans = get_bool('Create new vault? ')
        if ans:
            create_vault()


def create_vault():
    conn = sqlite3.connect(vault_file)
    conn.cursor().execute(create_table_sql).close()
