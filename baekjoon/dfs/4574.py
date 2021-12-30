# 스도미노쿠

import sys
def solve(can,table,empty) :
    if len(empty) == 0 : 
        for t in table : 
            print(''.join(map(str,t)))
        sys.exit(0)
    y,x = empty[0]
    dy = [-1,0,0,1]
    dx = [0,-1,1,0] 
    for d in range(4) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<9 and 0<=nx<9 and table[y][x] == 0 and table[ny][nx] == 0 :


input = sys.stdin.readline
dic = dict(zip(['A','B','C','D','E','F','G','H','I'],range(9)))
for th in range(2) : 
    N = int(input())
    table = [[0 for _ in range(9)] for _ in range(9)]
    can = []
    for i in range(1,10) : 
        for j in range(i+1,10) : 
            can.append([i,j])
    for _ in range(N) : 
        y,loc1,x,loc2 = map(str,input().split())
        can.remove(sorted([int(y),int(x)]))
        table[dic[loc1[0]]][int(loc1[1])-1] = int(y)
        table[dic[loc2[0]]][int(loc2[1])-1] = int(x)
    li = list(map(str,input().split()))
    num = 1
    for loc in li : 
        table[dic[loc[0]]][int(loc[1])-1] = num
        num += 1
    empty = []
    for y in range(9) : 
        for x in range(9) : 
            if table[y][x] == 0 : 
                empty.append([y,x])
    print('Puzzle ' + str(th+1))
    solve(can,table,empty)
dummy = input()
