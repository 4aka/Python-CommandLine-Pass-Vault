from VaultFeatures import search, create_entry, show_favorite, edit_entry
from Vault import login
import sys


def show_wellcome():
    print('''Wellcome to your VAULT!''')


def show_menu():
    action = input('''
    s - search
    c - create
    f - favorites
    e - edit
    z - exit
    ''')
    match action:
        case "s":
            search()
        case "c":
            create_entry()
        case "f":
            show_favorite()
        case "e":
            edit_entry()
        case "z":
            sys.exit()


def main():
    show_wellcome()
    login()
    show_menu()


# Run main
if __name__ == '__main__':
    main()
