import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
lst = []

for _ in range(n) :
    name = input().strip()
    dic[name] = 1

for _ in range(m) :
    name = input().strip()
    if name in dic :
        lst.append(name)

lst.sort()
print(len(lst))
print(*lst, sep="\n")