import random

ERROR_MESSAGE: str = "Incorrect"


def generate_password(length: int):
    password = generate_symbols(length)
    while password == ERROR_MESSAGE:
        password = generate_symbols(length)
    return generate_symbols(length)


def spec_symbols():
    return [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
            46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94,
            95, 96, 123, 124, 125, 126]


def is_pass_contains_all_important_parts(password):
    is_lower = False
    is_upper = False
    is_digit = False
    is_spec = False

    for char in password:
        if char.islower():
            is_lower = True
        if char.isupper():
            is_upper = True
        if char.isdigit():
            is_digit = True
        if ord(char) in spec_symbols():
            is_spec = True

    return is_lower and is_upper and is_digit and is_spec


def generate_symbols(length: int):
    password = ""
    random_gen = random.Random()

    for _ in range(length):
        action = random_gen.randint(0, 3)
        ascii_symbol = 0

        if action == 0:
            ascii_symbol = random_gen.randrange(97, 122)  # a - z. 97 - 122
        elif action == 1:
            ascii_symbol = random_gen.randrange(65, 90)  # A - Z. 65 - 90
        elif action == 2:
            ascii_symbol = random_gen.randint(48, 57)  # 0 - 9. 48 - 57
        else:
            ascii_symbol = spec_symbols()[
                random_gen.randint(0, len(spec_symbols()) - 1)]  # special symbol
        password += chr(ascii_symbol)
    if is_pass_contains_all_important_parts(password):
        return password
    else:
        return ERROR_MESSAGE
