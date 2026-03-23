lst = []

for _ in range(5):
    n = int(input())
    lst.append(max(n, 40))

print(sum(lst) // 5)