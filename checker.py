def retSubarr(arr,qs):
    length = len(arr)
    for i in qs:
        res=[]
        for j in range(length):
            for k in range(j,length):
                tempArr = arr[j:k] 
                if sum(tempArr)==i:
                    res.append(tempArr)
        if arr[-1]==i:
            res.append([arr[-1]])
        for i in res:
            print(i, end='')
        print()

t = int(input())
final=[]
for i in range(t):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    nq = int(input())
    q=[]
    for j in range(nq):
        q.append(int(input()))
    retSubarr(arr1,q)
