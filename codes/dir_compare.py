import os

def get_files_info(dir_path):
    files_info = {}
    
    with os.scandir(dir_path) as entries:
        for entry in entries:
            if entry.is_file():
                size = entry.stat().st_size
                
                with open(entry.path, "rb") as f:
                    content = f.read()
                
                files_info[entry.name] = (size, content)
    
    return files_info


def compare_directories(dir1, dir2):
    info1 = get_files_info(dir1)
    info2 = get_files_info(dir2)
    
    print(f"\n[{dir1}] 파일 개수: {len(info1)}")
    print(f"[{dir2}] 파일 개수: {len(info2)}")
    
    if len(info1) != len(info2):
        print("두 디렉토리의 파일 개수가 다릅니다.")
        return
    
    names1 = set(info1.keys())
    names2 = set(info2.keys())
    
    if names1 != names2:
        only_in_1 = names1 - names2 
        only_in_2 = names2 - names1
        if only_in_1:
            print(f"'{dir1}'에만 있는 파일: {only_in_1}")
        if only_in_2:
            print(f"'{dir2}'에만 있는 파일: {only_in_2}")
        return
    
    all_same = True
    for name in names1:
        size1, content1 = info1[name]
        size2, content2 = info2[name]
        
        if size1 != size2:
            print(f"→ '{name}' 크기가 다릅니다 ({size1} vs {size2})")
            all_same = False
        elif content1 != content2:
            print(f"→ '{name}' 내용이 다릅니다")
            all_same = False
    
    if all_same:
        print("\n동일합니다.")
    else:
        print("\n두 디렉토리에 차이가 있습니다.")


d1 = input("첫 번째 디렉토리? : ")
d2 = input("두 번째 디렉토리? : ")

path1 = os.path.join(os.getcwd(), d1)
path2 = os.path.join(os.getcwd(), d2)

compare_directories(path1, path2)