# 두 동전

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
N,M = map(int,input().split())
table = [[] for _ in range(N)]
for i in range(N) : 
    table[i] = [j for j in str(input())[:-1]]
dy = [0,0,1,-1]
dx = [-1,1,0,0]
balls = []
for y in range(N) : 
    for x in range(M) : 
        if table[y][x] == 'o' : 
            balls.append([y,x])
            table[y][x] = '.'
deq = deque()
deq.append([balls,0])
visited = []
visited.append(balls)
ans = sys.maxsize
while deq : 
    curr_balls,num = deq.popleft()
    if num > 10 : 
        continue
    for d in range(4) : 
        next = []
        out = 0
        flag = True
        for y,x in curr_balls : 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0<= nx < M : 
                if table[ny][nx] == '#' : 
                    next.append([y,x])
                elif table[ny][nx] == '.' : 
                    next.append([ny,nx])
            else : 
                out += 1
        next = sorted(next)
        if out == 1 : 
            if ans > num : 
                ans = num + 1
        elif out == 2 : 
            continue
        else : 
            if len(next) == 2 and next not in visited : 
                visited.append(next)
                deq.append([next,num+1])
if ans > 10 : 
    print(-1)
else : 
    print(ans)
