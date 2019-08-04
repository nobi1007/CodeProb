testCases = int(input().strip())
for iterations in range(testCases):
    n = int(input().strip())
    maxInt = 0
    minInt = 1000
    for i in range(n):
        tempInput = int(input().strip())
        if tempInput>maxInt:
           maxInt = tempInput
        if tempInput < minInt:
            minInt = tempInput
    print((maxInt//minInt)+(maxInt%minInt))
    print((maxInt//minInt)-(maxInt%minInt))
            
