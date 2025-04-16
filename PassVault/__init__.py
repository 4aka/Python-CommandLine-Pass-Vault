from VaultFeatures import search, create_entry, show_favorite, edit_entry
from Vault import login
import sys
from GeneratePassword import generate_password


def show_wellcome():
    print('''Wellcome to your VAULT!''')
    action = None

    while action != "z":

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
        if action == "z":
            sys.exit()


def main():
    login()
    show_wellcome()


# Run main
if __name__ == '__main__':
    main()
