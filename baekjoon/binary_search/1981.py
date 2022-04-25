# 배열에서 이동

import sys
from collections import deque

def bfs(left,right) : 
    if table[0][0] < left or table[0][0] > right :
        return False
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    start = [0,0]
    deq = deque()
    deq.append(start)
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    while deq : 
        y,x = deq.popleft()
        if y == n-1 and x == n-1 : 
            return True
        for d in range(4) : 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and left <= table[ny][nx] <= right : 
                visited[ny][nx] = True
                deq.append([ny,nx])
    return False

input = sys.stdin.readline
n = int(input())
table = []
for _ in range(n) : 
    table.append(list(map(int,input().split())))
start,end = 0,0
limit = max(map(max,table))
ans = sys.maxsize
while start <= limit and end <= limit : 
    if bfs(start,end) : 
        ans = min(ans,end - start)
        start += 1
    else : 
        end += 1
print(ans)