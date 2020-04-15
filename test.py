# cook your dish here
from math import gcd
for _ in range(int(input())):
    # a,b = input().strip().split()
    
    # a = list(a)
    # b = list(b)
    # maxi = 0
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         (a[i],b[j]) = (b[j],a[i])
    #         maxi = max(maxi,int("".join(a))+int("".join(b)))
    #         (a[i],b[j]) = (b[j],a[i])
    # print(maxi)

    # s = input().strip()
    # k,x = list(map(int,input().split()))
    
    # dic = {}
    # for i in range(len(s)):
    #     if k >= 0:
    #         if s[i] not in dic:
    #             dic[s[i]] = 1
    #         else:
    #             dic[s[i]] += 1
    #             if dic[s[i]] > x:
    #                 dic[s[i]] -= 1
    #                 k -= 1
    #     else:
    #         break
    # print(sum(dic.values()))
    
    n,m = list(map(int,input().split()))
    arr = list(set(map(int,input().split())))
    arr.sort()
    val = 1
    l = []
    for i in range(len(arr)):
        val = (val*arr[i])//gcd(val,arr[i])
        l.append(val)
    
    final = []
    maxi = val
    pos = 1
    for i in range(1,m+1):
        if val%i!=0:
            temp = (i*val)//gcd(i,val)
            if temp > maxi:
                maxi = temp
                pos = i
    print(pos)

# dinesh.jayakumar@focusacademy.in