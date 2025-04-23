import sqlite3
from Variables import passowrd_file, vault_file_path, vault_file, search_site


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


def get_unique_site_name():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()

    site = input('site: ')
    cursor.execute(search_site, (site,))
    conn.commit()
    entry = cursor.fetchone()

    # Define if site exists
    # TODO replace to assertions
    if entry is not None:
        while site is not None:
            site = input('Site has already existed! Create another name: ')
            cursor.execute(search_site, (site,))
            conn.commit()
            entry = cursor.fetchone()
            if entry is None:
                break

    return site


def passwords_equels(password_1, password_2):
    return password_1 == password_2
