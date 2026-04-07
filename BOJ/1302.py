n = int(input())
books = {}

for _ in range(n):
    book = input()

    if book not in books :
        books[book] = 1
    else :
        books[book] += 1

lst = list(books.items())
lst.sort(key=lambda x : (-x[1], x[0]))

print(lst[0][0])