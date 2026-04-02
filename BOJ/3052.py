lst = [0 for _ in range(42)]

for _ in range(10) :
    n = int(input())

    lst[n%42] = 1

print(sum(lst))
