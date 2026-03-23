int2 = input()

if int2 == '0' :
    print("0")
else :
    dic = {
        '000' : '0',
        '001' : '1',
        '010' : '2',
        '011' : '3',
        '100' : '4',
        '101' : '5',
        '110' : '6',
        '111' : '7'
    }

    if len(int2) % 3 == 1 :
        int2 = '00' + int2
    elif len(int2) % 3 == 2 :
        int2 = '0' + int2

    for i in range(0, len(int2), 3) :
        print(dic[int2[i:i+3]], end="")