hamburger_min = 99999
beverage_min = 99999

for _ in range(3) :
    n = int(input())
    if n <= hamburger_min :
        hamburger_min = n
        
for _ in range(2) :
    n = int(input())
    if n <= beverage_min :
        beverage_min = n
        
print(hamburger_min + beverage_min - 50)