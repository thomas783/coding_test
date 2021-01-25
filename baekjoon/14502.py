# 연구소

import sys
import copy
from collections import deque
def bfs(maps) : # 바이러스를 퍼뜨리는 함수
    global answer
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    deq = deque()
    for i in range(N) : 
        for j in range(M) :
            if maps[i][j] == 2 : 
                deq.append([i,j])
    while deq : 
        temp = deq.popleft()
        x,y = temp
        for idx in range(4) :
            if 0<=x+dx[idx]<N and 0<=y+dy[idx]<M and maps[x+dx[idx]][y+dy[idx]] == 0:
                maps[x+dx[idx]][y+dy[idx]] = 2
                deq.append([x+dx[idx],y+dy[idx]])
    result = 0
    for i in maps : 
        for j in i : 
            if j == 0 : 
                result += 1
    answer = max(result,answer)

def make_wall(maps,cnt) : # 벽 세우는 함수 재귀로 짬 
    if cnt == 3 : 
        new_map = copy.deepcopy(maps)
        bfs(new_map)
        return
    for i in range(N) : 
        for j in range(M) : 
            if maps[i][j] == 0 :
                maps[i][j] = 1
                make_wall(maps,cnt+1)
                maps[i][j] = 0

N ,M = map(int,sys.stdin.readline().rstrip().split(' '))
maps = []
for _ in range(N) : 
    maps.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
answer = 0
make_wall(maps,0)
print(answer)