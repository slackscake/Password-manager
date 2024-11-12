import json
import os
from base64 import encode

from rich import inspect
from cryptography.fernet import Fernet

from rich.tree import Tree
from rich import print


# key = Fernet.generate_key()
# cipher = Fernet(key)
#
# with open("key.key", "wb") as key_file:
#     key_file.write(key)

class Credentials:
    def __init__(self, web_id=None, create_user=None, create_password=None):
        self.web_id = web_id
        self.create_user = create_user
        self.create_password = create_password


    def users_input(self):
        self.web_id = input("WEB:")
        self.create_user = input("Login:")
        self.create_password = input("Password:")
        self.create_password = cipher.encrypt(self.create_password.encode())
        self.create_password = self.create_password.decode()
        return self.web_id, self.create_user, self.create_password

    def add_user(self):
        if os.path.exists("DateBase.json"):
            with open("DateBase.json", "r") as file:
                data = json.load(file)
        else:
            data = {}
        user_id = self.web_id
        new_user_data = {
            "user": self.create_user,
            "password": self.create_password
        }
        data[user_id] = new_user_data
        with open("DateBase.json", "w") as file:
            json.dump(data, file, indent=4)
        print("User saved")

    def read_user(self):
        with open("DateBase.json", "r")as file:
            data = json.load(file)
        sel_user = input("Type name of website to show user info:")
        if sel_user in data:
            decrypted_password = cipher.decrypt(data[sel_user]["password"])
            decrypted_password = decrypted_password.decode()
            data[sel_user]["password"] = decrypted_password
            tree = Tree("user")
            tree.add(sel_user)
            tree.add(data[sel_user]["user"])
            tree.add(data[sel_user]["password"])
            print(tree)
        elif sel_user == "all":
            tree = Tree("Пользователи")
            for user, info in data.items():
                user_branch = tree.add(user)  # Ветка для каждого пользователя
                for key, value in info.items():
                    user_branch.add(f"{key.capitalize()}: {value}")  # Добавляем информацию о пользователе
            print(tree)
        else:
            print("This user does not exist\nTry again")
    # def read_all_users(self):

with open("key.key", "r")as file:
    key = file.read()
cipher = Fernet(key)

b = Credentials()
# b.users_input()
# b.add_user()
b.read_user()

