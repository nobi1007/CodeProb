# from collections import deque

# Problem -

# Given a string find the no. of unique substrings which follow the given rule: (lengths of substring is 2 or 3 and adjacent substring should be different)

# INPUT               OUTPUT

# aaaaaa              (-1)
# aaaaa               aa aaa = (2)
# abcabc              ab ca bc = (3)
# abcabcbc            ab cab cbc, abc ab cbc = (4)


def getNumber (house):
    # Write your solution here.
    if len(house)<2:
        return 0
    else:
        i = 2
        l = [house[:2]]
        last = 2
        main = set()
        while i<len(house):
            if i+2 <= len(house) and house[i:i+2] != l[-1]:
                l.append(house[i:i+2])
                i += 2
                last = 2
                if i == len(house):
                    for j in l:
                        main.add(j)
                    l.pop()
                    l.pop()
                    i-=4
                    l.append(house[i:i+3])
                    i+=3 
            elif i+3 <= len(house) and house[i:i+3] != l[-1]:
                l.append(house[i:i+3])
                i += 3
                last = 3
                if i == len(house):
                    break
                # check = True
            else:
                # if check == False
                # i -= last
                # l.pop()
                if last == 2 and i+3<=len(house):
                    i -= 2
                    l.pop()
                    l.append(house[i:i+3])
                    i+=3
                elif last == 3:
                    i -= 3
                    l.pop()
                    if i <= 0:
                        break
            print(l)
        return len(main)
 
T = int(input())
for _ in range(T):
    house = input()
 
    out_ = getNumber(house)
    print (out_)