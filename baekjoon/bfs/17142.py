# 연구소 3

from itertools import combinations
import copy
from collections import deque
def bfs(area,virus) :
    deq = deque()
    virus = [[x,y,0] for x,y in virus]
    for v in virus : 
        deq.append(v)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    time = 0 # 시간을 따로 세줌
    while deq : 
        x,y,z = deq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N :
                if area[nx][ny] == 0 :  
                    area[nx][ny] = '*' # 자꾸 2랑 겹쳐서 바이러스 퍼지는걸 '*'로 표시함
                    deq.append([nx,ny,z+1])
                    time = max(time,z+1)
                elif area[nx][ny] == 2 : 
                    area[nx][ny] = '*'
                    deq.append([nx,ny,z+1])
    isTrue = True # 모두 바이러스로 채웠는지 확인
    for i in range(N) : 
        for j in range(N) : 
            if area[i][j] == 0 : 
                isTrue = False
                break
    if isTrue : 
        return time
    else : 
        return sys.maxsize # 못채웠다면 방해 안되도록 가장 큰수

import sys
N,M = map(int,sys.stdin.readline().rstrip().split(' '))
area = []
for _ in range(N) : 
    area.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
virus = []
for i in range(N) : 
    for j in range(N) : 
        if area[i][j] == 2 : 
            virus.append([i,j])
candidate = combinations(virus,M)
answer = sys.maxsize
for c in candidate :
    new_area = copy.deepcopy(area)
    temp_answer = bfs(new_area,c)
    answer = min(answer,temp_answer)
if answer == sys.maxsize : 
    print(-1)
else : 
    print(answer)