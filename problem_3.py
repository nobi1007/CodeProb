for _ in range(int(input().strip())):
    length,breadth = list(map(int,input().strip().split()))
    for i in range(length):
        if(i == 0 or i == length-1):
            print("# "*breadth)
        else:
            print("# "+"  "*(breadth-2)+"#")
