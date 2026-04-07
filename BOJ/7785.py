import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n) :
    name, log = input().split()
    
    dic[name] = log

lst = list(dic.items())
lst.sort(key=lambda x : x[0], reverse=True)

for name, log in lst :
    if log == "enter" :
        print(name)