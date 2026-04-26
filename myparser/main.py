import argparse
from pathlib import Path
from shlex import split
from myparser.Commands import commands, cd
import os
def manipulation():
    while(True):
        ip = input('')
        if ip=='quit' or ip=='exit':
            break
        
        tokens = split(ip)
        if len(tokens) == 3:
            command = tokens[0]
            flag = tokens[1]
            arguments = tokens[2]
        elif len(tokens) == 2:
            command = tokens[0]
            arguments = tokens[1]
        else:
            command = tokens[0]
        
        if command in commands:
            commands[command](arguments)
        else:
            print("Not a valid command")
        
        print('\n',Path.cwd(),'$>',end=' ')
        

def main():
    parser = argparse.ArgumentParser(
                    prog='main.py',
                    description='Start the CLI file manager',
                    epilog='End of the help!!')


    parser.add_argument(
        '-start_myp', '--myp', action='store_true', help='name of the folder or file'
    )
    args = parser.parse_args()
    
    os.chdir(r'C:\Users\manmo')
    
    if args.myp:
        print('\n',Path.cwd(),'$>',end=' ')
        manipulation()

if __name__ == '__main__':
    main()
