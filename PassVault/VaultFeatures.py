import sqlite3
from Variables import vault_file, create_entry_sql, search_sql, show_favorites_sql
from Vault import decrypt_password, copy_to_clipboard, get_bool, encrypt


def search():
    site = input('Search site: ')
    result = decrypt_password(db_search(site))
    print("Password copied to clipboard")
    copy_to_clipboard(result)


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


def show_favorite():
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(show_favorites_sql)
    conn.commit()
    conn.close()

    search()


def edit_entry():
    return None