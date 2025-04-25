import hashlib
import pyperclip
from Variables import hash_count


def hash_data(data):
    hashed_data = data
    for x in range(hash_count):
        hashed_data = hashlib.sha3_256(hashed_data.encode('ascii')).hexdigest()
    return hashed_data


def get_bool(prompt):
    while True:
        try:
            return {"y": True, "n": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input please enter y or n!")


def copy_to_clipboard(data):
    pyperclip.copy(data.decode())


def input_data(input_text):
    return input(input_text)
