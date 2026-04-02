c = int(input())

for _ in range(c) :
    line = list(map(int, input().split()))
    n = line[0]
    scores = line[1:]

    avg = sum(scores) / n
    cnt = 0

    for score in scores :
        if score > avg :
            cnt += 1

    print(f"{cnt/n * 100:.3f}%")
