for _ in range(int(input().strip())):
    inputString = input().strip()
    alpha = []
    num = []
    special = []
    for i in inputString:
        if i.isalpha():
            alpha.append(i)
        elif i.isnumeric():
            num.append(i)
        else:
            special.append(i)
    if len(alpha)>0:
        print("Alphabets are : " + "".join(alpha))
    else:
        print("Alphabets are : NONE")
    if len(num)>0:
        print("Numbers are : " + "".join(num))
    else:
        print("Numbers are : NONE")
    if len(alpha)>0:
        print("Special characters are : " + "".join(special))
    else:
        print("Special characters are : NONE")


        