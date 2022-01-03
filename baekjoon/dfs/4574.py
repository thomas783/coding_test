# 스도미노쿠

import sys
# 해당 위치에 넣은 숫자가 가능한지 확인하는 함수
def check(y,x,n,table) :
    # 같은 열 확인
    for k in range(9) : 
        if k != x and table[y][k] == n : 
            return False
    # 같은 행 확인
    for k in range(9) : 
        if k != y and table[k][x] == n : 
            return False
    # 같은 네모 확인
    for i in range(y//3*3,y//3*3+3) : 
        for j in range(x//3*3,x//3*3+3) : 
            if table[i][j] == n and (i != y or j != x) : 
                return False
    return True

def solve(can,table,empty) :
    if len(empty) == 0 : 
        for t in table : 
            print(''.join(map(str,t)))
        return
    y,x = empty[0]
    dy = [-1,0,0,1]
    dx = [0,-1,1,0] 
    flag = False
    for d in range(4) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<9 and 0<=nx<9 and table[y][x] == 0 and table[ny][nx] == 0 :
            for i in range(len(can)) : 
                num1,num2 = can[i]
                if check(y,x,num1,table) and check(ny,nx,num2,table) : 
                    flag = True
                    table[y][x], table[ny][nx] = num1,num2
                    if len(can) > 1 : 
                        can.remove([num1,num2])
                        empty.remove([ny,nx])
                        solve(can,table,empty[1:])
                        can.insert(i,[num1,num2])
                        empty.append([ny,nx])
                        table[y][x],table[ny][nx] = 0,0
                    else : 
                        solve(can,table,[])
                if check(y,x,num2,table) and check(ny,nx,num1,table) : 
                    flag = True
                    table[y][x], table[ny][nx] = num2,num1
                    if len(can) > 1 :
                        can.remove([num1,num2]) 
                        empty.remove([ny,nx])
                        solve(can,table,empty[1:])
                        can.insert(i,[num1,num2])
                        empty.append([ny,nx])
                        table[y][x],table[ny][nx] = 0,0
                    else : 
                        solve(can,table,[])
    if not flag : 
        return
input = sys.stdin.readline
dic = dict(zip(['A','B','C','D','E','F','G','H','I'],range(9)))
th = 1
while True : 
    N = int(input())
    if N == 0 : 
        break
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
    print('Puzzle ' + str(th))
    solve(can,table,empty)
    th += 1
sys.exit(0)