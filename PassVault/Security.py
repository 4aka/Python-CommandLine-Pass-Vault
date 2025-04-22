import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from PasswordActions import read_password_bytes
import base64

password_hash = read_password_bytes()


def derive_key(password_hash, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Довжина ключа для AES-256
        salt=salt,
        iterations=200000  # Збільште кількість ітерацій для більшої безпеки
    )
    key = kdf.derive(password_hash)
    return key


def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data


def save_data_to_db(username, password):
    date = os.urandom(16)
    key = derive_key(password_hash, date)
    key_b64 = base64.urlsafe_b64encode(key)
    encrypted_username = encrypt_data(username, key_b64)
    encrypted_password = encrypt_data(password, key_b64)

    # Зберігаємо в базу даних: salt, encrypted_username, encrypted_password
    print(
        f"Saving to DB: salt={date.hex()}, "
        f"encrypted_username={encrypted_username.hex()}, "
        f"encrypted_password={encrypted_password.hex()}")
    # Тут має бути код для збереження в базу даних


def get_data_from_db(username):

    salt = bytes.fromhex("your_salt_hex")  # Замінити на реальний salt з бази даних
    encrypted_username = b"your_encrypted_username"  # Замінити на реальний зашифрований username з бази даних
    encrypted_password = b"your_encrypted_password"  # Замінити на реальний зашифрований password з бази даних

    key = derive_key(password_hash, salt)
    key_b64 = base64.urlsafe_b64encode(key)
    decrypted_username = decrypt_data(encrypted_username, key_b64)
    decrypted_password = decrypt_data(encrypted_password, key_b64)
    return decrypted_username, decrypted_password


if __name__ == '__main__':
    print(password_hash)
    save_data_to_db("myusername", "mypassword")
    retrieved_username, retrieved_password = get_data_from_db("myusername")
    print(f"Retrieved username: {retrieved_username}, password: {retrieved_password}")
