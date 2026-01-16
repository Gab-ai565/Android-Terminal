import os


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

commands = {
    "ls": ls,
    "pwd": pwd,
}

while True:
    cmd = input(">> ").strip()

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


