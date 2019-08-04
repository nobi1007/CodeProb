for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = list(map(int,input().strip().split()))
    subArr = {}
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(arr[i:j]) in list(subArr.keys()):
                subArr[sum(arr[i:j])].append(arr[i:j])
            else:
                subArr[sum(arr[i:j])] = [arr[i:j]]
    q = int(input().strip())
    for x in range(q):
        query = int(input().strip())
        for i in subArr[query]:
            print(i,end = " ")
        print("",end="\n")
    
