# 아기 상어

import sys
from collections import deque
def bfs(y,x,size) : 
    global curr
    deq = deque()
    deq.append([y,x,0])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    can = []
    while deq : 
        dy = [0,0,1,-1]
        dx = [1,-1,0,0]
        y,x,cnt = deq.popleft()
        for d in range(4) : 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and table[ny][nx] <= size : 
                visited[ny][nx] = True
                deq.append([ny,nx,cnt+1])
                if 0< table[ny][nx] < size : 
                    can.append([ny,nx,cnt+1])
    if len(can) == 0 : 
        return 0
    else : 
        can = sorted(can,key = lambda x : (x[2],x[0],x[1]))[0]
        curr = can[:-1]
        table[curr[0]][curr[1]] = 0
        return can[-1]
    

input = sys.stdin.readline
n = int(input())
table = []
for _ in range(n) : 
    table.append(list(map(int,input().split())))
ans = 0
size = 2
for i in range(n) : 
    for j in range(n) : 
        if table[i][j] == 9 :
            curr = [i,j]
            table[i][j] = 0
curr_stomach = 0
while True : 
    cnt = bfs(curr[0],curr[1],size)
    if cnt == 0 : 
        print(ans)
        break
    else : 
        ans += cnt
        curr_stomach += 1
        if curr_stomach == size : 
            size += 1
            curr_stomach = 0