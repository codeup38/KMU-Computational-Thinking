n = int(input())
lst = []

for _ in range(n) :
    num = int(input())
    lst.append(num)

lst.sort()
print(*lst, sep='\n')