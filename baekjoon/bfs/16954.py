# 움직이는 미로 탈출

import sys
from collections import deque
from copy import deepcopy
# 벽이 움직이는 경우
def wall_move(table) : 
    new_table = deepcopy([['.' for _ in range(n)]] + table[:7])
    return new_table
# 욱제가 움직이는 경우
def move(y,x,table) : 
    global ans
    if table[y][x] == '#' : 
        return []
    dy = [1,1,1,0,0,0,-1,-1,-1]
    dx = [-1,0,1,-1,0,1,-1,0,1]
    can = []
    for d in range(9) : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=nx<n and 0<=ny<n and table[ny][nx] == '.' : 
            if ny == 0 and nx == n-1 : 
                ans = 1
                return
            can.append([ny,nx])
    return can

input = sys.stdin.readline
n = 8
table = []
for _ in range(n) : 
    table.append(list(map(str,input().rstrip())))
start = [n-1,0,table]
deq = deque()
deq.append(start)
visited = [start]
ans = 0
while deq :
    y,x,curr_table = deq.popleft()
    can = move(y,x,curr_table)
    if ans == 1 : 
        print(1)
        sys.exit(0)
    new_table = wall_move(curr_table)
    for i,j in can : 
        if [i,j,new_table] not in visited : 
            deq.append([i,j,new_table])
            visited.append([i,j,new_table])
print(0)
