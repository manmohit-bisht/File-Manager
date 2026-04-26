import os

def cd(path):
    os.chdir(path)

commands = {
    'cd' : cd,
}