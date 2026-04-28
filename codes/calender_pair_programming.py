n = int(input())
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

start_day = 4
n_start_day = (sum(months[:n]) + start_day) % 7

print("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")
print(" " * 3 * n_start_day, end="")

for i in range(1, months[n] + 1) :
    print(f"{i:2d}", end = " ")

    if (n_start_day + i) % 7 == 0:
        print()