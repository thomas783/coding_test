# 말이 되고픈 원숭이

import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
w,h = map(int,input().split())
table = []
for _ in range(h) : 
    table.append(list(map(int,input().split())))
dy = [0,0,1,-1]
dx = [1,-1,0,0]
dy2 = [-2,-2,-1,-1,1,1,2,2]
dx2 = [-1,1,-2,2,-2,2,-1,1]
deq = deque()
visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]
deq.append([0,0,k])
ans = sys.maxsize
while deq : 
    y,x,num = deq.popleft()
    if y == h-1 and x == w-1 : 
        ans = min(ans,visited[y][x][num])
    for d in range(4) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<h and 0<=nx<w and table[ny][nx] == 0 and visited[ny][nx][num] == 0 : 
            visited[ny][nx][num] = visited[y][x][num] + 1
            deq.append([ny,nx,num])
    if num > 0 :
        for d in range(8) : 
            ny = y + dy2[d]
            nx = x + dx2[d]
            if 0<=ny<h and 0<=nx<w and table[ny][nx] == 0 and visited[ny][nx][num-1] == 0 :
                visited[ny][nx][num-1] = visited[y][x][num] + 1
                deq.append([ny,nx,num-1])
if ans == sys.maxsize : 
    print(-1)
else : 
    print(ans)
