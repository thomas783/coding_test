# 연구소 2

import sys
from collections import deque
from itertools import combinations

def bfs(position) : 
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    deq = deque()
    for p in position : 
        deq.append(p+[0])
        visited[p[0]][p[1]] = 0
    while deq : 
        y,x,cnt = deq.popleft()
        for d in range(4) : 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<n and 0<=nx<n and visited[ny][nx] == -1 and table[ny][nx] == 0 :
                visited[ny][nx] = cnt + 1
                deq.append([ny,nx,cnt+1])
    result = 0
    for y in range(n) : 
        for x in range(n) : 
            if table[y][x] != 1 :
                if visited[y][x] == -1 : 
                    return -1
                else : 
                    result = max(result,visited[y][x])
    return result

n,m = map(int,input().split())
table = []
for _ in range(n) : 
    table.append(list(map(int,input().split())))
# position에 바이러스를 놓을 수 있는 위치를 저장하고 원래 
# 테이블은 0으로 바꿈
position = []
for i in range(n) : 
    for j in range(n) : 
        if table[i][j] == 2 : 
            position.append([i,j])
            table[i][j] = 0
ans = sys.maxsize
for c in combinations(position,m) : 
    tmp = bfs(c)
    if tmp == -1 : 
        continue
    else : 
        ans = min(ans,tmp)
if ans == sys.maxsize : 
    print(-1)
else : 
    print(ans)