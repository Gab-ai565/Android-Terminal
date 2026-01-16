import os
import hashlib
import sqlite3

conection  = sqlite3.connect("users.db")
cursor = conection.cursor()
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conection.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login_or_register(username, password):
    password_hash = hash_password(password)

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        if user[0] == password_hash:
            return 0
        else:
            print("Incorrect username or  password")
    else:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password_hash)
        )
        conection.commit()
        return 0


def ls():
    print(os.listdir())


def pwd():
    print(os.getcwd())


def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("Directory not found")


def mkdir(name):
    os.mkdir(name)


def rmdir(name):
    os.rmdir(name)


def help():
    print("""ls: show items in the directory
pwd:  shows the directory 
cd: change directory 
mkdir: create directory
rmdir: delete directory 
quit: exit the program
""")

commands = {
    "ls": ls,
    "pwd": pwd,
    "help": help
}

username = input("Your username: ")
password = input("Your password: ")

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
conection.commit()

while True:
    cmd = input(username + "~$ ").strip()

    if cmd == "quit":
        print("Exiting...")
        break

    parts = cmd.split()
    command = parts[0]

    if command in commands:
        commands[command]()

    elif command == "cd":
        if len(parts) > 1:
            cd(parts[1])
        else:
            print("Usage: cd <directory>")

    elif command == "mkdir":
        if len(parts) > 1:
            mkdir(parts[1])

    elif command == "rmdir":
        if len(parts) > 1:
            rmdir(parts[1])

    else:
        print("Error: Command does not exist")


