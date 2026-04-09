m = int(input())
n = int(input())

def valid(num) :
    if num == 1 :
        return False
        
    for i in range(2, num) :
        if num % i == 0 :
            return False
    
    return True

min_ = 1e9
sum_ = 0

for i in range(m, n+1) :
    if valid(i) :
        min_ = min(min_, i)
        sum_ += i

if min_ == 1e9 :
    print(-1)
else :
    print(sum_)
    print(min_)