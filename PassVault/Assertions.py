from Variables import passowrd_file
from Variables import vault_file_path


def is_password_file_exists():
    try:
        if open(passowrd_file, "r").readable():
            return True
    except FileNotFoundError as e:
        print('There is no any created vaults. Create vault')


def is_vault_file_exists():
    try:
        if open(vault_file_path, "r").readable():
            return True
    except FileNotFoundError as e:
        print('There is no any created vaults')

