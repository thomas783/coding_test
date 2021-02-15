# 아기 상어

# 0 : 빈칸, 1,2,3,4,5,6 : 물고기 크기, 9 : 아기 상어 위치
import sys
from collections import deque

def bfs(area,cur) : 
    can = []
    visited = [cur]
    deq = deque()
    deq.append(cur+[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while deq : 
        x,y,d = deq.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and [nx,ny] not in visited :
                if area[nx][ny] == 0 or area[nx][ny] == cur_size : # 빈칸이거나 크기가 같은 물고기라 그냥 지나가는 경우
                    visited.append([nx,ny])
                    deq.append([nx,ny,d+1])
                elif 0<area[nx][ny]<cur_size : # 물고기를 먹으러 간경우
                    visited.append([nx,ny])
                    can.append([nx,ny,d+1])
    return can

N = int(input())
area = []
for _ in range(N) : 
    area.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
fish = []
answer = 0
cur_size = 2 # 아기 상어 초기 크기
cur_stomach = 0 # 아기 상어가 먹은 물고기 개수
for i in range(N) : 
    for j in range(N) :
        if 1<=area[i][j]<=6 : 
            fish.append([i,j])
        elif area[i][j] == 9 : 
            cur_loc = [i,j]
            area[i][j] = 0 
while bfs(area,cur_loc) : 
    temp = sorted(bfs(area,cur_loc),key = lambda x : (x[2],x[0],x[1]))[0]
    area[temp[0]][temp[1]] = 0
    cur_loc = temp[:2]
    answer += temp[2]
    cur_stomach += 1
    if cur_stomach == cur_size : 
        cur_size += 1
        cur_stomach = 0
print(answer)