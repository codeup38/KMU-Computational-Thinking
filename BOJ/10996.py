n = int(input())

for _ in range(n) :
    for i in range(n) :
        if i % 2 == 0 :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()
    for i in range(n) :
        if i % 2 == 1 :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()
    