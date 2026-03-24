N = int(input())
cnt = 0
num = N

while True :
    if num < 10 :
        num = num + num * 10
    else :
        num = (num // 10 + num % 10) % 10 + (num % 10) * 10

    cnt += 1

    if num == N :
        break

print(cnt)
