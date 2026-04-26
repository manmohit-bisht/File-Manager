import argparse
from pathlib import Path
from shlex import split
from myparser.Commands import commands, cd
import os


def manipulation():
    while True:

        # Handling user Input and Tokenization
        userInput = input("")
        if userInput == "quit" or userInput == "exit":
            break

        tokens = split(userInput)
        command = tokens[0]
        flags = [word for word in tokens[1:] if word.startswith("-")]
        arguments = [word for word in tokens[1:] if not word.startswith("-")]

        # Executing commands
        if command in commands:
            commands[command](arguments, flags)
        else:
            print("Not a valid command, please enter a valid command")

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
