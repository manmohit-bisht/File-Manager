import os
from pathlib import Path

# from myparser.Flags import flags


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

    # Applying flag effects
    items = []
    if not "-hidden" in flags:
        items = [item for item in p.iterdir() if not item.name.startswith(".")]
    else:
        items = list(p.iterdir())

    if "-asc" in flags and "-desc" in flags:
        print("Conflicting flags")
        return
    if "-asc" in flags:
        items.sort()
    if "-desc" in flags:
        items.sort(reverse=True)
    if "-full" in flags:
        for item in items:
            print(item)
    else:
        for item in items:
            print(item.name)


# fmt: off

commands = {
    "cd": cd, 
    "listdir": listdir
    }

# fmt: on
