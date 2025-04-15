import Vault as vault
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
            vault.search()
        case "c":
            vault.create_entry()
        case "f":
            vault.show_favorite()
        case "e":
            vault.edit_entry()
        case "z":
            sys.exit()


def main():
    show_wellcome()
    vault.login()
    show_menu()


# Run main
if __name__ == '__main__':
    main()
