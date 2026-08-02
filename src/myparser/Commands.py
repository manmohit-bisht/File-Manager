import os
from pathlib import Path
from .registry import command


@command("cd", allowed_flags=[])
def cd(arguments, flags):
    if not arguments:
        print("cd: missing path!! Please enter a valid path")
    elif flags:
        print("Invalid command no flags must be given")
    else:
        os.chdir(arguments[0])


@command("listdir", allowed_flags=["-full", "-asc", "-desc", "-hidden"])
def listdir(arguments, allowed_flags):
    if not arguments:
        path = Path.cwd()
    else:
        path = arguments[0]
    p = Path(path)

    # Applying flag effects
    items = []
    if not "-hidden" in allowed_flags:
        items = [item for item in p.iterdir() if not item.name.startswith(".")]
    else:
        items = list(p.iterdir())
    if "-asc" in allowed_flags and "-desc" in allowed_flags:
        print("Conflicting allowed_flags")
        return
    if "-asc" in allowed_flags:
        items.sort()
    if "-desc" in allowed_flags:
        items.sort(reverse=True)
    if "-full" in allowed_flags:
        print("")
        for item in items:
            print(item)
    else:
        print("")
        for item in items:
            print(item.name)


# fmt: off

# commands = {
#     "cd": cd, 
#     "listdir": listdir
#     }

# fmt: on
