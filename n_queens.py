n = int(input())
visited_cols = [0 for i in range(n)]
positions = []
for col in range(n):
    visited_cols = [0 for i in range(n)]
    visited_cols[col] = 1
    r = 2
    op = find_pos(n,r,positions,visited_cols)
    if op[0]:
        print(op[1])
        

def find_pos(n,r,positions,visited_cols):
    
    

    if r==8 and len(positions)!=n:
        return (0,positions)
    else:
        return 1
    
                                                                                                                    