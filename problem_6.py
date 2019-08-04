from math import sqrt as sq
def isPrime(x):
    token = 0
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,int(sq(x))+2):
            if x%i == 0:
                token = 0
                break
            else:
                token = 1
        if token == 0:
            return False
        else:
            return True
for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int,input().strip().split()))
    dic = {}
    for i in arr:
        if i in list(dic.keys()):
            dic[i] += 1
        else:
            if isPrime(i):
                dic[i] = 1
    maxI = max(list(dic.values()))
    lfinal = []
    for i in list(dic.keys()):
        if dic[i] == maxI:
            lfinal.append(i)
    print(" ".join(list(map(str,list(sorted(lfinal))))))
    
