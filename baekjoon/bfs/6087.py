# 레이저 통신

import sys
from collections import deque
input = sys.stdin.readline
w,h = list(map(int,input().split()))
table = []
for _ in range(h) : 
    table.append(list(map(str,input().rstrip())))
lazer = []
for i in range(h) : 
    for j in range(w) : 
        if table[i][j] == 'C' : 
            lazer.append([i,j])
start,end = lazer[0],lazer[1]
deq = deque()
# i는 그전에 온 방향, 0은 설치된 거울의 갯수
for i in range(4) : 
    deq.append(start + [i,0])
visited = [[sys.maxsize for _ in range(w)] for _ in range(h)]
visited[start[0]][start[1]] = 0
dy = [-1,1,0,0]
dx = [0,0,1,-1]
while deq : 
    curr_y,curr_x,dir,cnt = deq.popleft()
    ny = curr_y + dy[dir]
    nx = curr_x + dx[dir]
    while 0<=ny<h and 0<=nx<w :
        if table[ny][nx] == '.' or table[ny][nx] == 'C' : 
            if visited[ny][nx] > cnt + 1 : 
                # 상하에서 왔다면 좌우로 좌우에서 왔다면 상하로 보냄
                for d in range((1 - dir // 2) * 2, (1 - dir // 2) * 2 + 2) : 
                    deq.append([ny,nx,d,cnt+1])
                    visited[ny][nx] = cnt + 1
            ny += dy[dir]
            nx += dx[dir]
        elif table[ny][nx] == '*' : 
            break
print(visited[end[0]][end[1]]-1)