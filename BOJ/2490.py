ref = ["D","C","B","A","E"]

for _ in range(3):
    lst = list(map(int, input().split()))

    print(ref[sum(lst)])
    
