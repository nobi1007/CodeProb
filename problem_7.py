t = int(input().strip())
for i in range(t):
    n,k = list(map(int,input().strip().split()))
    if n%(k*k) == 0:
        print("NO")
    else:
        print("YES")

