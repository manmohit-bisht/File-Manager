import argparse
from pathlib import Path
from shlex import split
import os
import myparser.commands
from myparser.registry import COMMAND_REGISTRY


def manipulation():
    while True:
        # Handling user Input and Tokenization
        userInput = input("").strip()
        if not userInput:
            continue
        if userInput == "quit" or userInput == "exit":
            break

        tokens = split(userInput, posix=False)
        cmd_name = tokens[0]
        arguments = [word for word in tokens[1:] if not word.startswith("-")]
        arguments = [arg.strip('"') for arg in arguments]
        flags = [word for word in tokens[1:] if word.startswith("-")]
        print(tokens)
        print(arguments)
        print(flags)
        # Executing commands
        if cmd_name not in COMMAND_REGISTRY:
            print("Not a valid command, please enter a valid command")
            print("\n", Path.cwd(), ">>", end=" ")
            continue

        cmd_info = COMMAND_REGISTRY[cmd_name]

        invalid_flags = [f for f in flags if f not in cmd_info["flags"]]
        if invalid_flags:
            print(f"Invalid flag(s) for '{cmd_name}': {', '.join(invalid_flags)}")
            print("\n", Path.cwd(), ">>", end=" ")
            continue

        cmd_info["func"](arguments, flags)
        print("\n", Path.cwd(), ">>", end=" ")


def main():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Start the CLI file manager",
        epilog="End of the help!!",
    )

    parser.add_argument(
        "-start", "--myp", action="store_true", help="name of the folder or file"
    )
    args = parser.parse_args()

    os.chdir(r"C:\Users\manmo")

    if args.myp:
        print("\n", Path.cwd(), ">>", end=" ")
        manipulation()


if __name__ == "__main__":
    main()
