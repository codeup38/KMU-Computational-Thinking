n = int(input())

for _ in range(n) :
    line = input()

    streak = 0
    score = 0

    for i,c in enumerate(line) :
        if c == 'O' :
            streak += 1
            score += streak
        else :
            streak = 0
    
    print(score)
            