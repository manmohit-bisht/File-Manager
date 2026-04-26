import os
from pathlib import Path


def cd(arguments, flags):
    if not arguments:
        print("cd: missing path!! Please enter a valid path")
    elif flags:
        print("Invalid command no flags must be given")
    else:
        os.chdir(arguments[0])


def listdir(arguments, flags):
    if not arguments:
        path = Path.cwd()
    else:
        path = arguments
    p = Path(path)
    for item in p.iterdir():
        print(item.name)


# fmt: off

commands = {
    "cd": cd, 
    "listdir": listdir
    }

# fmt: on
