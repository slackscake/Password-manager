import bcrypt
import json

try:
    with open("user.json", "r") as file:
        crypt_user = json.load(file)
    str_login = crypt_user["login"]
    str_password = crypt_user["password"]

    bytes_login = str_login.encode()
    bytes_password = str_password.encode()

    def check_input(input_login, input_password):
        login_match = bcrypt.checkpw(input_login.encode(), bytes_login)
        password_match = bcrypt.checkpw(input_password.encode(), bytes_password)
        return login_match and password_match

except FileNotFoundError:
    print("There is not registered user\nPlease enter Login and Password to register a new user")
    login = input("Login: ")
    password = input("Password:")

    hashed_login = bcrypt.hashpw(login.encode(), bcrypt.gensalt())
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    hashed_login_str = hashed_login.decode()
    hashed_password_str = hashed_password.decode()

    hash_dict = {"login" : hashed_login_str, "password" : hashed_password_str}
    with open("user.json", "w") as file:
        json.dump(hash_dict, file)
    input(f"Registration was successful\nRemember Login:{login} Password:{password}\n\nPress any key")

