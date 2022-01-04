# 벽 부수고 이동하기 4

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
table = []
for _ in range(n) : 
    table.append([int(i) for i in input()[:-1]])
for i in range(n) : 
    for j in range(m) : 
        if table[i][j] == 1 : 
            table[i][j] = -1
dy = [0,0,1,-1]
dx = [1,-1,0,0]
ans_table = [[0 for _ in range(m)] for _ in range(n)]
num = 0
for i in range(n) : 
    for j in range(m) : 
        if table[i][j] == -1 :
            ans_table[i][j] = -1
        elif table[i][j] == 0 : 
            start = [i,j]
            visited = [start]
            deq = deque()
            deq.append(start)
            while deq : 
                y,x = deq.popleft()
                for d in range(4) :
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0<=ny<n and 0<=nx<m and [ny,nx] not in visited and table[ny][nx] == 0 : 
                        deq.append([ny,nx])
                        visited.append([ny,nx])
            import pdb; pdb.set_trace()
            for v1,v2 in visited : 
                ans_table[v1][v2] = [len(visited),num]
            num += 1
ans = [[0 for _ in range(m)] for _ in range(n)]
for a in ans_table : 
    print(a)
for y in range(n) : 
    for x in range(m) : 
        if ans_table[y][x] == -1 : 
            s = 1
            tmp = []
            for d in range(4) : 
                ny = y + dy[d]
                nx = x + dx[d]
                if 0<=ny<n and 0<=nx<m and ans_table[ny][nx] != -1 :
                    if ans_table[ny][nx][1] not in tmp :  
                        s += ans_table[ny][nx][0]
                        tmp.append(ans_table[ny][nx][1])
            ans[y][x] = s % 10
for a in ans : 
    print(a)