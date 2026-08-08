import os
from pathlib import Path
from .registry import command
from shutil import rmtree


@command("cd", allowed_flags=[])
def cd(arguments, allowed_flags):
    if not arguments:
        print("cd: missing path!! Please enter a valid path")
        return
    if len(arguments) != 1:
        print("Please enter only 1 argument")
        return
    if allowed_flags:
        print("Invalid command: no flags must be given")
        return

    path = Path(arguments[0])

    if not path.exists():
        print("Please enter a valid path that exists")
        return

    if not path.is_dir():
        print("Error: path is not a directory")
        return
    try:
        os.chdir(path)
    except PermissionError:
        print("Permission denied")
    except OSError as e:
        print(f"Unable to change directory: {e}")


@command("listdir", allowed_flags=["-full", "-asc", "-desc", "-hidden"])
def listdir(arguments, allowed_flags):
    if len(arguments) > 1:
        print("Invalid number of arguments")
        return
    if not arguments:
        path = Path.cwd()
    else:
        path = arguments[0]
    path = Path(path)
    if not path.exists() or not path.is_dir():
        print("Enter a valid path to a directory!!")
        return
    # Applying flag effects
    items = []
    if not "-hidden" in allowed_flags:
        items = [item for item in path.iterdir() if not item.name.startswith(".")]
    else:
        items = list(path.iterdir())
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


@command("rename", allowed_flags=[])
def rename(arguments, allowed_flags):
    if len(arguments) != 2:
        print("Enter valid number of arguments!! Usage: rename <old_name> <new_name>")
        return

    if allowed_flags:
        print("This command does not accept flags.")
        return

    old_path = Path(arguments[0]).expanduser()
    new_path = Path(arguments[1]).expanduser()

    if not old_path.exists():
        print("Source file does not exist.")
        return

    if new_path.exists():
        print("Destination already exists.")
        return

    try:
        old_path.rename(new_path)
        print("Renamed")
    except PermissionError:
        print("Permission denied.")
    except OSError as e:
        print(f"Rename failed: {e}")


@command("execute", allowed_flags=[])
def execute(arguments, allowed_flags):
    if len(arguments) != 1:
        print("Error: Enter 1 valid argument!")
        return

    if allowed_flags:
        print("This command doesn't accept flags")
        return

    path = Path(arguments[0])
    if not path.exists():
        print("Enter a valid path to a file!!")
        return
    if not path.is_file():
        print("Error: in which OS can you execute a folder!!")
        return
    try:
        os.startfile(path)
    except OSError as e:
        print(f"Execution failed: {e}")


@command("mkdir", allowed_flags=[])
def mkdir(arguments, allowed_flags):
    if len(arguments) != 1:
        print("Enter Destination Address-: mkdir <destination_address>")
        return
    if allowed_flags:
        print("This command doesn't except any flags")
        return
    destination = arguments[0]
    try:
        Path(destination).mkdir(parents=True, exist_ok=False)
        print("Created")
    except FileExistsError:
        print("Directoy already exists")
    except PermissionError:
        print("You don't have persmission to create folder here")
    except OSError as e:
        print(f"ERROR: {e}")


@command("mkfile", allowed_flags=[])
def mkfile(arguments, allowed_flags):
    if len(arguments) != 1:
        print("ERROR: mkfile <file name or file path>")
        return
    if allowed_flags:
        print("This command doesn't except any flags")
        return
    file = Path(arguments[0])
    try:
        file.touch(exist_ok=False)
        print("Created")
    except FileNotFoundError:
        print("The Destination Address couldn't be found")
    except FileExistsError:
        print("This file already exists in the destination")
    except PermissionError:
        print("You don't have the permission to create file here")
    except OSError as e:
        print(f"ERROR: {e}")


@command("delfile", allowed_flags=[])
def delfile(arguments, allowed_flags):
    if len(arguments) != 1:
        print("ERROR: delfile <file name or file path>")
        return
    if len(allowed_flags) > 1:
        print("This command doesn't except any flags")
    destination = Path(arguments[0])
    try:
        destination.unlink()
        print("Deleted")
    except FileNotFoundError:
        print("File couldn't be found")
    except PermissionError:
        print("Don't go deleting any files 🥹: you don't have permission b****")
    except OSError as e:
        print(f"ERROR: {e}")


@command("deldir", allowed_flags=["-all"])
def deldir(arguments, allowed_flags):
    if len(arguments) != 1:
        print("ERROR: deldir <file name or file path>")
        return
    destination = Path(arguments[0])
    if not "-all" in allowed_flags:
        try:
            destination.rmdir()
            print("Deleted")
        except FileNotFoundError:
            print("destination address couldn't be fount")
        except PermissionError:
            print("Don't go deleting any folders 🥹: you don't have permission b****")
        except OSError as e:
            print(f"ERROR: {e}")
    else:
        msg = "Type this msg to delete, type anything else to revoke-: \nI reallly want to delete it"
        print(msg, "\n")
        usermsg = input("")
        if usermsg == "I reallly want to delete it":
            print("\nAre you reallly sure, you can't recover it. yes/no")
            newmsg = input()
            if newmsg == "yes":
                try:
                    rmtree(destination)
                    print("Deleted")
                except FileNotFoundError:
                    print("The folder couldn't be found at designated address")
                except PermissionError:
                    print(
                        "Don't go deleting any folders 🥹: you don't have permission b****"
                    )
                except OSError as e:
                    print(f"ERROR: {e}")
            elif newmsg == "no":
                print("ok")
                return
            else:
                print(
                    "I don't know what gibberish is that but i will take that as a no-: 😏"
                )
                return
        else:
            return


@command("cls", allowed_flags=[])
def cls(arguments, allowed_flags):
    if arguments or allowed_flags:
        print("this command doesn't accept any arguments or flags")
        return
    print("\033[H\033[2J", end="", flush=True)
