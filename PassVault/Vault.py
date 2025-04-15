from Assertions import is_password_file_exists
from PasswordActions import (
    compare_passwords, compare_password_with_existed,
    create_password, read_db_password, create_db_password)
from cryptography.fernet import Fernet
from Variables import (
    vault_file, create_entry_sql,
    search_sql, create_table_sql, show_favorites_sql)
from HashData import hash_data
import sqlite3
import pyperclip


def login():
    if is_password_file_exists():
        existed_user_scenario()
    else:
        new_user_scenario()


def search():
    site = input('Search site: ')
    result = decrypt_password(db_search(site))
    print("Password copied to clipboard")
    copy_to_clipboard(result)


def get_bool(prompt):
    while True:
        try:
            return {"y": True, "n": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input please enter True or False!")


def create_entry():
    site = input('Fill in site name or URL: ')
    username = input('Fill in username: ')
    password = input(b'Fill in password: ')
    is_favorite = get_bool('Add entry to favorite? y/n: ')

    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    encrypted_password = encrypt(password)
    cursor.execute(create_entry_sql(site, username, encrypted_password, is_favorite))
    conn.commit()
    conn.close()


def show_favorite():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(show_favorites_sql)
    conn.commit()
    conn.close()

    search()


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


def copy_to_clipboard(data):
    pyperclip.copy(data)


def db_search(site):
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(search_sql, site)
    result = cursor.fetchone()
    conn.close()
    if result:
        return decrypt_password(result[0])
    else:
        return None


def decrypt_password(encrypted_password):
    f = Fernet(read_db_password())
    return f.decrypt(encrypted_password).decode()


def create_vault():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()


def encrypt(data):
    key = read_db_password()
    f = Fernet(key)
    return f.encrypt(data)


def decrypt(data):
    key = read_db_password()
    f = Fernet(key)
    return f.decrypt(data)


def edit_entry():
    return None