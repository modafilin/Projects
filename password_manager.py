from cryptography.fernet import Fernet

# This creates a key.key file
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:     
        key_file.write(key)"""

#  This encrypts the password
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

# This allows to view the username and the password
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

# This allows you to add a username and the password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

# This opens/creates a text file and adds new name and enrypted password to the text document
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# This is basically the main menu
while True:
    mode = input("Would you like to add a new password or review the existing ones? (view, add) press q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
    