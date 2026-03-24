s = input()
summ = 0

for c in s :
    if 'a' <= c <= 'z' :
        summ += ord(c) - 96
    else :
        summ += ord(c) - 64 + 26

if summ == 1 :
    print("It is a prime word.")
else :
    for i in range(2, summ) :
        if summ % i == 0 :
            print("It is not a prime word.")
            break
    else :
        print("It is a prime word.")