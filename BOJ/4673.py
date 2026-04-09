self_nums = [1 for _ in range(10001)]

def d(n) :
    new_num = n + sum(map(int, list(str(n))))
    if new_num <= 10000 :
        self_nums[new_num] = 0
        d(new_num)
    else :
        return

for i in range(1, 10001) :
    d(i)

for i in range(1, 10001) :
    if self_nums[i] == 1 :
        print(i)
