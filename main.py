import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='main.py',
                    description='Prints the parent directory',
                    epilog='End of the help!!')


parser.add_argument(
    "-pd", "--file", metavar="folder_or_file_name",required=True, help="name of the folder or file"
)

args = parser.parse_args()

parent_dir = Path(args.file).resolve().parent

print("Path to parent directory: ",parent_dir)


