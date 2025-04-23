import os
import sqlite3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from Variables import vault_file, select_date, hash_count_db, date_db
from PasswordActions import read_password_bytes
import base64


def derive_key(password_hash: bytes, date: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=date,
        iterations=hash_count_db
    )
    key = kdf.derive(password_hash)
    return key


def encrypt_data(data, key) -> bytes:
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode('utf-8'))
    return encrypted_data


def decrypt_data(encrypted_data: bytes, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data


def encryptV2(username: str, password: str):
    date = os.urandom(date_db)

    password_hash = read_password_bytes()

    key = derive_key(password_hash, date)
    key_b64 = base64.urlsafe_b64encode(key)

    encrypted_username = encrypt_data(username, key_b64)
    encrypted_password = encrypt_data(password, key_b64)

    if username != '' and password != '':
        return encrypted_username, encrypted_password, date
    elif username != '':
        return encrypted_username, date
    elif password != '':
        return encrypted_password, date


def decryptV2(date, encrypted_data):
    password_hash = read_password_bytes()
    key = derive_key(password_hash, date)
    key_b64 = base64.urlsafe_b64encode(key)

    decrypted_data = decrypt_data(encrypted_data, key_b64)
    return decrypted_data


def get_date(site: str) -> bytes:
    conn = sqlite3.connect(vault_file)
    cursor = conn.cursor()
    cursor.execute(select_date, (site,))
    conn.commit()

    date = cursor.fetchone()
    conn.close()
    return date[0]
