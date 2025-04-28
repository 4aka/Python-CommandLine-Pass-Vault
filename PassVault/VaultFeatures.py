import sqlite3
import sys

from Assertions import is_site_name_unique, is_username_empty, is_vault_empty
from Variables import (vault_file, show_favorites_sql, create_entry_sql, search_site, select_is_favorite, delete_row, update_favorites)
from Tools import get_bool, copy_to_clipboard
from GeneratePassword import generate_password
from Security import encryptV2, decryptV2, get_date


def search():
    if is_vault_empty():
        return

    # Get site name
    site = input('Search site: ')
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()

    # Get password
    cursor.execute(search_site, (site,))
    entry = cursor.fetchone()
    conn.close()

    # Decrypt
    if entry:
        usrnm = decryptV2(get_date(site), entry[2]).decode()  # [2] - usrnm
        pswd = decryptV2(get_date(site), entry[3])  # [3] - pswd
        copy_to_clipboard(pswd)
        print('Username: ' + usrnm)
        print("### Password copied to clipboard")
    else:
        print("There is no such site")


def create_entry():
    # Collect data
    site = is_site_name_unique()
    username = is_username_empty()
    is_favorite = get_bool('Add to favorite? y/n: ')

    if get_bool('Generate password? y/n: '):
        password = generate_password(20)
    else:
        password = input('Create your password: ')

    # Encryption
    (filed_username, field_password, date) = encryptV2(username, password)

    # Add to db
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(create_entry_sql, (site, date, filed_username,
                                      field_password, is_favorite))
    conn.close()


def show_favorite():
    if is_vault_empty():
        return

    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(show_favorites_sql)
    entry = cursor.fetchall()
    conn.close()

    if len(entry) > 0:
        for i in entry:
            print(i[0])
    else:
        print('Favorites is empty')
        return


def edit_entry():
    if is_vault_empty():
        return

    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()

    site = input('Search site to edit entry: ')
    entry = cursor.execute(search_site, (site,)).fetchone()
    while entry is None:
        site = input('There is no such site, try again: ')
        entry = cursor.execute(search_site, (site,)).fetchone()

    # Collect data
    username = decryptV2(get_date(site), entry[2]).decode()
    password = decryptV2(get_date(site), entry[3]).decode()
    cursor.execute(select_is_favorite, (site,))
    is_favorite = cursor.fetchone()[0]

    if get_bool('Change username? y/n: '):
        new_username = input('Add new username: ')
        (filed_username, field_password, date) = (
            encryptV2(new_username, password))

        cursor.execute(delete_row, (site,))
        cursor.execute(create_entry_sql, (site, date,
                                          filed_username, field_password, is_favorite))
        print('### New username added and saved')

    if get_bool('Change password? y/n: '):
        (filed_username, field_password, date) = encryptV2(username, generate_password(20))

        cursor.execute(delete_row, (site,))
        cursor.execute(create_entry_sql, (site, date, filed_username,
                                          field_password, is_favorite))
        print('### New password generated and saved')

    if input('Add to favorites? y/n: ') == "y":
        cursor.execute(update_favorites, (site,))
        print('### Entry added to favorites')

    conn.close()


def delete_entry():
    if is_vault_empty():
        return

    site = input('Search url to delete entry: ')
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(search_site, (site,))
    entry = cursor.fetchone()

    if entry:
        if get_bool('Delete ' + site + '? y/n: '):
            cursor.execute(delete_row, (site,))
            conn.close()
        print(site + ' entry deleted!')
    else:
        print('There is no entry with name: ' + site)
        return


def close_vault():
    sys.exit()
