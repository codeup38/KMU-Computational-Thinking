n = int(input())

for _ in range(n) :
    stack = []
    s = input()

    for c in s :
        # print(c, stack)
        if c == '(' :
            stack.append(c)
        else :
            if stack == [] :
                print("NO")
                break
            else :
                stack.pop()
    else :
        if stack == [] :
            print('YES')
        else :
            print('NO')