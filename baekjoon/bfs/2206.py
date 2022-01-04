# 벽 부수고 이동하기

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
table = []
for _ in range(n) : 
    table.append([int(i) for i in input()[:-1]])
start = [0,0,0,1]
ans = sys.maxsize
deq = deque()
deq.append(start)
dy = [0,0,1,-1]
dx = [1,-1,0,0]
# 벽을 부수지 않고 가는 경우와 벽을 부수고 가는 경우
visited = [[[sys.maxsize,sys.maxsize] for _ in range(m)] for _ in range(n)]
while deq : 
    y,x,boom,num = deq.popleft()
    if y == n-1 and x == m-1 : 
        ans = min(ans,num)
        continue
    for d in range(4) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<n and 0<=nx<m :
            # 벽을 부수고 왔고 앞으로 벽을 부수지 않는 경우 
            if boom == 1 and table[ny][nx] == 0 and visited[ny][nx][1] > num + 1 : 
                deq.append([ny,nx,boom,num+1]) 
                visited[ny][nx][1] = num + 1
            # 벽을 부수지 않고 왔고 앞으로 벽을 부수지 않는 경우
            elif boom == 0 and table[ny][nx] == 0 and visited[ny][nx][0] > num + 1 : 
                deq.append([ny,nx,boom,num+1])
                visited[ny][nx][0] = num + 1
            # 벽을 부수지 않고 왔고 앞으로 벽을 부술 경우
            elif boom == 0 and table[ny][nx] == 1 and visited[ny][nx][1] > num +1 : 
                deq.append([ny,nx,1,num+1])
                visited[ny][nx][1] = num + 1
if ans == sys.maxsize : 
    print(-1)
else : 
    print(ans)