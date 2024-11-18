import bcrypt
import json
import os
from cryptography.fernet import Fernet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class UserAuth:
    def __init__(self):
        self.user_file = "user.json"
        self.load_user()

    def load_user(self):
        try:
            with open(self.user_file, "r") as file:
                crypt_user = json.load(file)
            self.bytes_login = crypt_user["login"].encode()
            self.bytes_password = crypt_user["password"].encode()
        except FileNotFoundError:
            self.register_new_user()

    def check_input(self, input_login, input_password):
        login_match = bcrypt.checkpw(input_login.encode(), self.bytes_login)
        password_match = bcrypt.checkpw(input_password.encode(), self.bytes_password)
        return login_match and password_match

    def register_new_user(self):
        clear_screen()
        print("There is no registered user\nPlease enter Login and Password to register a new user\n")
        login = input("Login: ")
        password = input("Password: ")
        clear_screen()

        hashed_login = bcrypt.hashpw(login.encode(), bcrypt.gensalt())
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        hash_dict = {
            "login": hashed_login.decode(),
            "password": hashed_password.decode()
        }

        with open(self.user_file, "w") as file:
            json.dump(hash_dict, file)

        print(f"Registration was successful\nRemember your \nLogin:{login} and password:{password}\n\n")
        input("Press any key to continue")

        self.bytes_login = hashed_login
        self.bytes_password = hashed_password

# Использование класса
auth = UserAuth()
