from VaultFeatures import search, create_entry, show_favorite, edit_entry, delete_entry, close_vault
from Vault import login

__author__ = "Arch Incorp"
__copyright__ = "Copyright 2025, The Vault Project"
__credits__ = "Arch Incorp"
__maintainer__ = "Arch Incorp"
__email__ = "7nuclear@gmail.com"
__status__ = "Testing"


def main():
    login()
    menu()


def menu():
    print('''Wellcome to your VAULT!\n''')
    action = None

    while action != "z":
        action = input('''
        s - search
        c - create
        f - favorites
        e - edit
        d - delete
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
            case "d":
                delete_entry()
        if action == "z":
            close_vault()


# Run main
if __name__ == '__main__':
    main()
