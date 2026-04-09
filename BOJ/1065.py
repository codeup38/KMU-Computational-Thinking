n = int(input())
cnt = 0

def check(num) :
    if num < 100 :
        return True

    lst = list(map(int, str(num)))
    diff = lst[1] - lst[0]

    for i in range(len(lst) - 1) :
        if lst[i+1] - lst[i] != diff :
            return False
    
    return True
            

for i in range(1, n + 1) :
    if check(i) :
        cnt += 1

print(cnt)