for _ in range(int(input())):
    s = list(input().strip())
    stack = []
    stack.append(s[0])
    for i in s[1:]:
        if len(stack)>0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        print("true")
    else:
        print("false")



