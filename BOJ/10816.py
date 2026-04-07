import sys 
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dic = {}

m = int(input())
query = list(map(int, input().split()))

for num in lst :
    if num not in dic :
        dic[num] = 1
    else :
        dic[num] += 1

for num in query :
    if num in dic :
        print(dic[num], end=" ")
    else : 
        print(0, end=" ")