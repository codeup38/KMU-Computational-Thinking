A, B = map(int,input().split())

if A > B:
    A, B = B, A

n = (B - A) + 1
print((A + B) * n // 2)