from Variables import passowrd_file, vault_file_path, passowrd_db_file


def is_password_file_exists():
    try:
        if open(passowrd_file, "r").readable():
            return True
    except FileNotFoundError as e:
        print('There is no password')


def is_db_password_file_exists():
    try:
        if open(passowrd_db_file, "r").readable():
            return True
    except FileNotFoundError as e:
        print('There is no password')


def is_vault_file_exists():
    try:
        if open(vault_file_path, "r").readable():
            return True
    except FileNotFoundError as e:
        print('There is no any created vaults')

