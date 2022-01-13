# 로봇 청소기

import sys
from collections import deque
from itertools import permutations
def bfs(start,target) :
    deq = deque()
    deq.append(start)
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    visited[start[0]][start[1]] = 0
    while deq : 
        y,x = deq.popleft()
        for d in range(4) : 
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<h and 0<=nx<w and visited[ny][nx] == -1 :
                if ny == target[0] and nx == target[1] : 
                    return visited[y][x] + 1
                elif table[ny][nx] == '.' : 
                    deq.append([ny,nx])
                    visited[ny][nx] = visited[y][x] + 1
    return -1

input = sys.stdin.readline
dy = [0,0,1,-1]
dx = [1,-1,0,0]
while True : 
    w,h = map(int,input().split())
    if w == 0 and h == 0 : 
        sys.exit(0)
    table = []
    for _ in range(h) : 
        table.append(list(map(str,input().rstrip())))
    # 로봇의 시작 위치 확인
    trash = []
    for i in range(h) : 
        for j in range(w) : 
            if table[i][j] == 'o' : 
                start = [i,j]
                table[i][j] = '.'
            elif table[i][j] == '*' : 
                table[i][j] = '.'
                trash.append([i,j])
    trash = [start] + trash
    dist = [[0 for _ in range(len(trash))] for _ in range(len(trash))]
    flag = True
    for i in range(len(trash)) : 
        for j in range(len(trash)) : 
            dist[i][j] = bfs(trash[i],trash[j])
            if i != j and dist[i][j] == -1 :
                flag = False
    if not flag : 
        print(-1)
        continue
    ans = sys.maxsize
    for p in permutations(list(range(1,len(trash)))) : 
        p = [0] + list(p)
        tmp = 0
        for i in range(len(p)-1) : 
            if dist[i][i+1] >= 0 : 
                tmp += dist[p[i]][p[i+1]]
            else : 
                ans = sys.maxsize
                break
        ans = min(ans,tmp)
    print(ans)