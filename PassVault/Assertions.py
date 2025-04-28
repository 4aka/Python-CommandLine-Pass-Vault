import sqlite3

import regex

from Variables import passowrd_file, vault_file_path, vault_file, search_site, select_all


def is_password_file_exists():
    try:
        if open(passowrd_file, "r").readable():
            return True
    except FileNotFoundError as e:
        print('There is no password')


def is_vault_file_exists():
    try:
        if open(vault_file_path, "r").readable():
            return True
    except FileNotFoundError:
        print('There is no any created vaults')


def is_site_name_unique():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()

    site = input('site: ')
    while site == '':
        site = input('Site should be a string! Try again: ')
        if site != '':
            break

    cursor.execute(search_site, (site,))
    entry = cursor.fetchone()

    # Define if site exists
    if entry is not None:
        while site is not None:
            site = input('Site has already existed! Create another name: ')
            cursor.execute(search_site, (site,))
            entry = cursor.fetchone()
            if entry is None:
                break
    conn.close()
    return site


def is_username_empty():
    username = input('Username: ')

    if username == '':
        while username == '':
            username = input('Username should be a string! Try again: ')
            if username != '':
                break
    else:
        return username


def passwords_equels(password_1, password_2):
    return password_1 == password_2


def is_vault_empty():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(select_all)
    entry = cursor.fetchone()
    conn.close()
    if entry is None:
        print('Vault is empty! Create at list one entry')
        return True
    else:
        return False


def assert_input(prompt):
    data = input(prompt)
    input_data = regex.search(r'\p{IsCyrillic}', data)

    if input_data is not None:
        while input_data is not None:
            print('Wrong locale. Only English allowed!')
            data = input(prompt)
            input_data = regex.search(r'\p{IsCyrillic}', data)
            if input_data is None:
                return data
    else:
        return data
