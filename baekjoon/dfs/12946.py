# 육각 보드

def dfs(y,x,c) : 
    global final_ans
    dy = [-1,-1,0,0,1,1]
    dx = [0,1,-1,1,0,-1] 
    color[y][x] = c
    final_ans = max(final_ans,1)
    for d in range(6) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<N and 0<=nx<N : 
            if table[ny][nx] == 'X' :
                if color[ny][nx] == -1 : 
                    dfs(ny,nx,1-c)
                    final_ans = max(final_ans,2)
                elif color[ny][nx] == c : 
                    final_ans = max(final_ans,3)
                    return

import sys
from copy import deepcopy
sys.setrecursionlimit(5000)
input = sys.stdin.readline
N = int(input())
table = []
for _ in range(N) : 
    table.append(list(input())[:-1])
color = [[-1 for _ in range(N)] for _ in range(N)]
final_ans = 0
for i in range(N) : 
    for j in range(N) : 
        if table[i][j] == 'X' and color[i][j] == -1 : 
            dfs(i,j,0)
print(final_ans)