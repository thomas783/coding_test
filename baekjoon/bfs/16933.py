# 벽 부수고 이동하기 3

import sys
from collections import deque
input = sys.stdin.readline
n,m,k = map(int,input().split())
table = []
for _ in range(n) : 
    table.append([int(i) for i in input()[:-1]])
start = [0,0,0,True,1]
ans = sys.maxsize
deq = deque()
deq.append(start)
dy = [0,0,1,-1,0]
dx = [1,-1,0,0,0]
# 3차원 그래프를 통해 벽을 몇번 부수고 도착했는지를 저장
visited = [[[sys.maxsize for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
while deq : 
    y,x,boom,flag,num = deq.popleft()
    if y == n-1 and x == m-1 : 
        visited[y][x][boom] = num
        continue
    for d in range(4) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<n and 0<=nx<m :
            # 부술 수 있는 벽이 없는 경우
            if boom == k and table[ny][nx] == 0 and visited[ny][nx][boom] > num + 1 : 
                deq.append([ny,nx,boom,not flag,num+1])
                visited[ny][nx][boom] = num + 1
            # 부술 벽이 남은 경우
            if boom < k :
                # 앞으로 벽을 부수는 경우
                if table[ny][nx] == 1 and visited[ny][nx][boom+1] > num + 1 and flag : 
                    deq.append([ny,nx,boom+1,not flag,num+1])
                    visited[ny][nx][boom+1] = num + 1
                # 앞으로 벽을 부수지 않는 경우
                elif table[ny][nx] == 0 and visited[ny][nx][boom] > num + 1 :
                    deq.append([ny,nx,boom,not flag,num+1])
                    visited[ny][nx][boom] = num + 1
                # 벽을 부수고 싶지만 대기하는 상태
                if table[ny][nx] == 1 and visited[ny][nx][boom+1] > num + 2 and not flag : 
                    deq.append([y,x,boom,not flag,num+1])
for i in visited[n-1][m-1] :
    ans = min(ans,i)
if ans == sys.maxsize : 
    print(-1)
else : 
    print(ans)