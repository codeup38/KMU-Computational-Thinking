c = {1,2,3}
d = {1,2,3}

try:
    print(c+d)
except TypeError :
    print("무엇이 문제일까? 'print(c+d)' 중 무엇을 고쳐야 하나?")
    print(c | d)