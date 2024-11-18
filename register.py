import json
import os
from cryptography.fernet import Fernet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        try:
            with open("DateBase.json", "r")as file:
                data = json.load(file)
            sel_web = input("For display all registered websites type 'all'\nType name of website to show user info:")
            if sel_web in data:
                clear_screen()
                decrypted_password = cipher.decrypt(data[sel_web]["password"])
                decrypted_password = decrypted_password.decode()
                data[sel_web]["password"] = decrypted_password
                print("Web:",sel_web, "\nUser:", data[sel_web]["user"], "\nPassword:", data[sel_web]["password"])

            elif sel_web == "all":
                clear_screen()
                for info in data:
                    print(info)

            else:
                print("This user does not exist\nTry again")
        except:
            print("Not websites have been created yet\nYou can create a website using the 'register' command")

with open("key.key", "r")as file:
    key = file.read()
cipher = Fernet(key)
