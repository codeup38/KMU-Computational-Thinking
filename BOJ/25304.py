X = int(input())
N = int(input())

summ = 0

for _ in range(N):
    a, b = map(int, input().split())
    summ += a*b

if summ == X:
    print("Yes")
else:
    print("No")

