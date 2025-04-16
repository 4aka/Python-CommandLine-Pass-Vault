import sqlite3
from Variables import vault_file, create_entry_sql, search_sql, show_favorites_sql
from Vault import decrypt, copy_to_clipboard, get_bool, encrypt


def search():
    site = input('Search site: ')

    result = None
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(search_sql, site)
    entry = cursor.fetchone()
    conn.close()
    if entry:
        result = decrypt(entry[0])

    print("Password copied to clipboard")
    copy_to_clipboard(result)


def create_entry():
    site = input('URL: ')
    username = input('Username: ')
    password = input('Password: ').encode()
    is_favorite = get_bool('Favorite? y/n: ')

    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    encrypted_password = encrypt(password)
    cursor.execute(create_entry_sql, (site, username, encrypted_password, is_favorite))
    conn.commit()
    conn.close()


def show_favorite():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(show_favorites_sql)
    conn.commit()
    conn.close()

    search()


def edit_entry():
    return None