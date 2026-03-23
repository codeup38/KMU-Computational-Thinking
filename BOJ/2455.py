people_max = 0
people_cur = 0

for _ in range(4) :
    down, up = map(int, input().split())
    people_cur -= down
    people_cur += up
    people_max = max(people_max, people_cur)

print(people_max)
