import sqlite3
from Variables import vault_file, show_favorites_sql, create_entry_sql, search_sql
from Vault import decrypt, copy_to_clipboard, get_bool, encrypt
from GeneratePassword import generate_password


def search():
    site = input('Search site: ')

    result = None
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(search_sql, ('%' + site + '%',))
    entry = cursor.fetchone()
    conn.close()
    if entry:
        result = decrypt(entry[0])
    copy_to_clipboard(result)
    print("Password copied to clipboard")


def create_entry():
    site = input('URL: ')
    username = input('Username: ').encode()
    password = generate_password(20)
    print('Generated password: ' + password)
    is_favorite = get_bool('Favorite? y/n: ')

    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    encrypted_password = encrypt(password.encode())
    encrypted_username = encrypt(username)
    cursor.execute(create_entry_sql, (site, encrypted_username, encrypted_password, is_favorite))
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
    site = input('Input url to edit entry: ')
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(search_sql, ('%' + site + '%',))


