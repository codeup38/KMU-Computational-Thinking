import sys 
input = sys.stdin.readline

K, L = map(int, input().split())

check = set()
lst = []
reversed_res = []

for _ in range(L):
    num = input().strip()
    lst.append(num)

for i in range(L-1, -1, -1) :
    num = lst[i]
    if num not in check :
        check.add(num)
        reversed_res.append(num)

res = reversed_res[-1:-K-1:-1]
print(*res, sep="\n")