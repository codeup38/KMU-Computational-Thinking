N = int(input())

minn = 10000

for i in range(0, N // 5 + 1) :
    for j in range(0, N // 3 + 1) :
        if i * 5 + j * 3 == N :
            minn = min(minn, i + j)

if minn == 10000 :
    print(-1)
else :
    print(minn)