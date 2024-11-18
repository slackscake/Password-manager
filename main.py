# V 0.1
# Создание системы верификации для входа в менеджер паролей

import os
from verification import UserAuth
import register as commands
import genpass as passg
from verification import UserAuth

entry = commands.Credentials()

auth = UserAuth()

# эта функция очищяет экран при вызове
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
user_login = input("Username: ")
user_password = input("Password: ")

if auth.check_input(user_login, user_password):
    clear_screen()
    print("To get help type 'help'")
    while True:
        command = input("$")
        clear_screen()
        # add new user
        if command == "register":
            entry.users_input()
            entry.add_user()
        # read user
        elif command == "list":
            entry.read_user()
        # password generator
        elif command == "genpass":
            passg.inp()
        # help print
        elif command == "help":
            print("Type 'register' to register a new user\n"
                  "Type 'list' to display the user\n"
                  "Type 'genpass' to generate random password.\n"
                  "To exit the program type !end")
        # close program
        elif command == "!end":
            break
        else:
            print("!!!No such command!!!")

else:
    print("Wrong login or password")