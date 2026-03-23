A, B = map(int, input().split())
C = int(input())

out_B = (B+C) % 60
out_A = (A + (B+C) // 60) % 24

print(out_A, out_B)
