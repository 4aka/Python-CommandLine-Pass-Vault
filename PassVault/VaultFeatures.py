import sqlite3
from Assertions import get_unique_site_name
from Variables import (vault_file, show_favorites_sql, create_entry_sql, search_site, select_is_favorite, delete_row)
from Vault import copy_to_clipboard, get_bool
from GeneratePassword import generate_password
from Security import encryptV2, decryptV2, get_date


def search():
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
        result = decryptV2(get_date(site), entry[3])  # [3] - pass
        copy_to_clipboard(result)
        print("Password copied to clipboard")
    else:
        print("Nothing found")


def create_entry():
    # Prepare data
    site = get_unique_site_name()
    username = input('Username: ')
    password = None
    is_favorite = get_bool('Add to favorite? y/n: ')

    gen_pass = get_bool('Generate password? y/n: ')
    if gen_pass:
        password = generate_password(20)
        print_pass = get_bool('Show password? y/n: ')
        if print_pass:
            print(f'Password: ' + password)
    else:
        password = input('Create your password: ')

    # Encryption
    (filed_username, field_password, date) = encryptV2(username, password)

    # Execute query
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(create_entry_sql, (site, date, filed_username, field_password, is_favorite))
    conn.commit()
    conn.close()


def show_favorite():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(show_favorites_sql)
    entry = cursor.fetchall()
    print(entry)
    conn.commit()
    conn.close()
    print()
    search()


def edit_entry():
    site = input('Search url to edit entry: ')
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(search_site, (site,))
    conn.commit()
    entry = cursor.fetchone()

    # Collect data
    username = decryptV2(get_date(site), entry[2]).decode()
    password = decryptV2(get_date(site), entry[3]).decode()
    cursor.execute(select_is_favorite, (site,))
    is_favorite = cursor.fetchone()[0]

    # Edit password
    result_is_password = input('Change password? Enter - no/ add - y: ')
    if result_is_password == "y":
        (filed_username, field_password, date) = encryptV2(username, generate_password(20))

        cursor.execute(delete_row, (site,))
        cursor.execute(create_entry_sql, (site, date, filed_username, field_password, is_favorite))
        conn.commit()
        print('New password generated and saved')

    # TODO Add data(salt)
    # Edit is_favorite
    result_is_favorite = input('Add to favorites? Enter - no/ add - y: ')
    if result_is_favorite == "y":
        cursor.execute('UPDATE vault SET is_favorite = TRUE WHERE site = ?', (site,))
        conn.commit()

    conn.close()


def delete_entry():
    site = input('Search url to edit entry: ')
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(delete_row, (site,))
    conn.commit()
    conn.close()
    print(site + 'has deleted!')
