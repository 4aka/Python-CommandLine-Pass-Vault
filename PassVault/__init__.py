from VaultFeatures import search, create_entry, show_favorite, edit_entry, delete_entry
from Vault import login
import sys
from GeneratePassword import generate_password

'''
    TODO
    
    Безпека ключа: Найважливіше – безпечно зберігати ключ AES. Не зберігайте його в коді або в тому ж файлі, 
    що й паролі. Розгляньте можливість використання ключа, який вводить користувач, або зашифруйте ключ іншим ключем.

    Salt: Використовуйте salt для захисту від атак за допомогою райдужних таблиць. Salt – це випадковий рядок, 
    який додається до пароля перед хешуванням.

    Key Derivation Function (KDF): Використовуйте KDF, таку як PBKDF2 або Argon2, 
    для отримання ключа AES з пароля користувача. Це робить атаку грубою силою більш складною.

    Обробка помилок: Додайте обробку помилок для обробки випадків, 
    коли файл не знайдено, ключ недійсний або виникають інші проблеми.

    Тестування: Ретельно протестуйте свій менеджер паролів, щоб переконатися, що він безпечний і надійний.
'''


def main():
    login()
    menu()


def menu():
    print('''Wellcome to your VAULT!''')
    action = None

    while action != "z":
        action = input('''
        s - search
        c - create
        f - favorites
        e - edit
        z - exit
        d - delete
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
            sys.exit()


# Run main
if __name__ == '__main__':
    main()
