import os

def listAll(path):
    print(path)
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                listAll(entry.path)   

base = input()
listAll(base)