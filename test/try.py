import os

base = input()

def search_dir(path) :
    try :
        list_dir = os.listdir(path)
    except PermissionError :
        print(f"[error] {path} is no permit to read file")
        return

    subdirs = [path + '/' + x for x in list_dir if os.path.isdir(path + '/' + x)]
    print(path)

    for subdir in subdirs :
        search_dir(subdir)
    

search_dir(base)