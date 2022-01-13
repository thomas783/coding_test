# 아기 상어 2

import sys
from collections import deque

def bfs(y,x) : 
    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]
    deq = deque()
    deq.append([y,x])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[y][x] = 0
    while deq : 
        y,x = deq.popleft()
        for d in range(8) : 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<n and 0<=nx<m :
                if table[ny][nx] == 0 and visited[ny][nx] == -1 :
                    deq.append([ny,nx])
                    visited[ny][nx] = visited[y][x] + 1
                elif table[ny][nx] == 1 and visited[ny][nx] == -1 : 
                    return visited[y][x] + 1

input = sys.stdin.readline
n,m = map(int,input().split())
table = []
for _ in range(n) : 
    table.append(list(map(int,input().split())))
ans = 0
for y in range(n) : 
    for x in range(m) : 
        if table[y][x] == 0 : 
            ans = max(ans,bfs(y,x))
print(ans)