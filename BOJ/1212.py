int_8 = input()

num_list = {"0":"000", "1":"001", "2":"010", "3":"011", "4":"100", "5":"101", "6":"110", "7":"111"}

if int_8 == "0":
    print("0")
else :
    for i,n in enumerate(int_8):
        tmp = num_list[n]

        if i == 0 :
            print(tmp.lstrip("0"), end="")
        else :
            print(tmp, end="")  