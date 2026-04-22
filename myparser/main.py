import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
                    prog='main.py',
                    description='Prints the parent directory',
                    epilog='End of the help!!')


    parser.add_argument(
        "-pd", "--file", metavar="folder_or_file_name", help="name of the folder or file"
    )

    parser.add_argument(
        '-cwd', "--cwd", action="store_true" ,help="Prints the current working directory"
    )
    args = parser.parse_args()

    if args.file:
        parent_dir = Path(args.file).resolve().parent
        print(parent_dir)
    if args.cwd:
        print(Path.cwd())

if __name__ == "__main__":
    main()
