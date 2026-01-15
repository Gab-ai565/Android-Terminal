import os

def ls():
    print(os.listdir())

def pwd():
    print(os.getcwd())

commands = {
    "ls": ls,
    "pwd": pwd
}

while True:
    cmd = input(">> ")

    if cmd == "quit":
        print("Leaving... ")
        break
    elif cmd in commands:
        commands[cmd]()
    else:
        print("Error: Command Does Not Exist")
