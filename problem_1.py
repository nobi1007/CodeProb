for _ in range(int(input().strip())):
    inputString = input().strip().split()
    print("%s%s%s"%(inputString[0]," "*(30-len(inputString[0])-len(inputString[1])),inputString[1]))
