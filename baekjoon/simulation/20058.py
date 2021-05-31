import sys
from copy import deepcopy
from collections import deque

def rotate(L,table) : 
    val = 2 ** L
    start = [0,0]
    x_start,y_start = 0,0
    x_end,y_end = 2 ** L,2 ** L
    temp_table = [[0 for _ in range(2**L)] for _ in range(2**L)]
    while x_end <= len(table) and y_end <= len(table) :  
        for x,tx in zip(range(x_start,x_end),range(val)) :
            for y,ty in zip(range(y_start,y_end),range(val)) :
                temp_table[tx][ty] = table[x][y]         
        temp_table = [list(i)[::-1] for i in zip(*temp_table)]
        for x,tx in zip(range(x_start,x_end),range(val)) :
            for y,ty in zip(range(y_start,y_end),range(val)) :
                table[x][y] = temp_table[tx][ty]
        if y_end != len(table) : 
            y_start += val
            y_end += val
        else : 
            y_start = 0
            y_end = val
            x_start += val
            x_end += val

def bfs(table) : 
    maximum = 0
    visited = [[False] * (2**N) for _ in range(2**N)]
    bigq = deque()
    for i in range(2**N) : 
        for j in range(2**N) : 
            bigq.append([i,j])
    while bigq : 
        i,j = bigq.popleft()
        if not visited[i][j] and table[i][j] != 0 : 
            visited[i][j] = True
            count = 1
            q = deque()
            q.append([i,j])
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            while q : 
                x,y = q.popleft()
                for d in range(4) : 
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<=nx<2**N and 0<=ny<2**N and not visited[nx][ny] and table[nx][ny] > 0 : 
                        count += 1
                        q.append([nx,ny])
                        visited[nx][ny] = True
            maximum = max(maximum, count)
    return maximum
        
input = sys.stdin.readline
global N
N,Q = list(map(int,input().split()))
table = []
for _ in range(2**N) : 
    table.append(list(map(int,input().split())))
step = list(map(int,input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for q in range(Q) : 
    L = step[q]
    rotate(L,table)
    melt = []
    for x in range(2**N) : 
        for y in range(2**N) : 
            if table[x][y] == 0 : 
                continue
            count = 0
            for d in range(4) : 
                nx = x + dx[d]
                ny = y + dy[d]
                if 0<=nx<2**N and 0<=ny<2**N and table[nx][ny] > 0 :
                    count += 1
            if count < 3 :
                melt.append([x,y])
    for x,y in melt : 
        table[x][y] -= 1
answer1 = 0
for i in range(2**N) : 
    for j in range(2**N) : 
        answer1 += table[i][j]
print(answer1)
print(bfs(table))
