import os

def print_all_txt(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                print_all_txt(entry.path)
            
            elif entry.is_file() and entry.name.endswith(".txt"):
                print(f"\n===== {entry.path} =====")
                with open(entry.path, "r") as f:
                    print(f.read())

base = input("폴더 경로 입력: ")
print_all_txt(base)
