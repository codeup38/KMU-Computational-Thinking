n, k = map(int, input().split())
maxi = 0

for i in range(1, k + 1) :
    num = n * i
    num = int(str(num)[::-1])
    maxi = max(maxi, num)

print(maxi)