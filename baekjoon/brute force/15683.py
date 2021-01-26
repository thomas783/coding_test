# 감시
# pypy3으로 제출, python3는 시간초과...

import sys, copy
from collections import deque
def fill(maps,dir,x,y) : # 원하는 방향으로 #을 채워주는 함수
    if dir == 4 :
        dir = 0
    elif dir == 5 : 
        dir = 1
    dx = [0,1,0,-1] # dir가 0:right,1:down,2:left,3:up
    dy = [1,0,-1,0]
    next_x = x + dx[dir]
    next_y = y + dy[dir]
    new_map = copy.deepcopy(maps)
    while 0<=next_y<M and 0<=next_x<N and new_map[next_x][next_y] != 6 :
        new_map[next_x][next_y] = '#'
        next_x += dx[dir]
        next_y += dy[dir]
    return new_map

def check(maps,cctv) : 
    global answer
    new_cctv = copy.deepcopy(cctv)
    if new_cctv : 
        temp = new_cctv.popleft()
        cctv_num = temp[0]
        x,y = temp[1:]
        if cctv_num == 1 : 
            for i in range(4) : 
                temp_map = fill(maps,i,x,y)
                check(temp_map,new_cctv)
        elif cctv_num == 2 : 
            for i in range(2) : 
                temp_map = fill(maps,i,x,y)
                temp_map = fill(temp_map,i+2,x,y)
                check(temp_map,new_cctv)
        elif cctv_num == 3 : 
            for i in range(4) : 
                temp_map = fill(maps,i,x,y)
                temp_map = fill(temp_map,i+1,x,y)
                check(temp_map,new_cctv)
        elif cctv_num == 4 : 
            for i in range(4) : 
                temp_map = fill(maps,i,x,y)
                temp_map = fill(temp_map,i+1,x,y)
                temp_map = fill(temp_map,i+2,x,y)
                check(temp_map,new_cctv)
        else : 
            temp_map = fill(maps,0,x,y)
            temp_map = fill(temp_map,1,x,y)
            temp_map = fill(temp_map,2,x,y)
            temp_map = fill(temp_map,3,x,y)
            check(temp_map,new_cctv)
    else : 
        temp_answer = 0
        for i in range(N) : 
            for j in range(M) : 
                if maps[i][j] == 0 :
                    temp_answer += 1
        answer = min(answer,temp_answer)

N,M = list(map(int,sys.stdin.readline().rstrip().split(' ')))
maps = []
for _ in range(N) : 
    maps.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
cctv = deque()
can = list(range(1,6))
for i in range(N) : # cctv의 번호와 위치를 저장
    for j in range(M) : 
        if maps[i][j] in can : 
            cctv.append([maps[i][j],i,j])
answer = N * M
check(maps,cctv)
print(answer)