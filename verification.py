import bcrypt
import json


with open("open.json", "r") as file:
    crypt_user = json.load(file)

str_login = crypt_user["login"]
str_password = crypt_user["password"]

bytes_login = str_login.encode()
bytes_password = str_password.encode()


def check_input(input_login, input_password):
    login_match = bcrypt.checkpw(input_login.encode(), bytes_login)
    password_match = bcrypt.checkpw(input_password.encode(), bytes_password)
    return login_match and password_match
