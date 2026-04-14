import sys
sys.setrecursionlimit(10**6)

n = int(input())
memo = {1:1, 2:1}

def fibo(n):
    if n in memo :
        return memo[n]
    else :
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

print(fibo(n))