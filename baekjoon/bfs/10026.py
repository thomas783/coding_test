# 적록색약

import sys
from collections import deque
from copy import deepcopy
def bfs(table) : 
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    num = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            if not visited[i][j] : 
                color = table[i][j]
                deq = deque()
                deq.append([i,j])
                visited[i][j] = True
                while deq : 
                    y,x = deq.popleft()
                    for d in range(4) : 
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0<=ny<n and 0<=nx<n and table[ny][nx] == color and not visited[ny][nx] : 
                            visited[ny][nx] = True
                            deq.append([ny,nx])
                num += 1
    return num

input = sys.stdin.readline
n = int(input())
table = []
for _ in range(n) : 
    table.append(list(map(str,input().rstrip())))
# 적록이 아닌 사람의 경우
ans1 = bfs(table)
# 적록인 사람의 경우
for i in range(n) : 
    for j in range(n) : 
        if table[i][j] == 'R' : 
            table[i][j] = 'G'
ans2 = bfs(table)
print(ans1,ans2)