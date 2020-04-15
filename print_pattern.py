n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    arr[0][i] = i+1
for i in range(1,n):
    for j in range(n):
        if i == j:
            arr[i][j] = i+j + 2
        else:
            tot = 0
            for k in range(n):
                if j!=k:
                    tot += arr[i-1][k]
            arr[i][j] = tot
for i in arr:
    for j in i:
        print(j,end=" ")
    print()
