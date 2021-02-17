# 미세먼지 안녕!

import sys
import copy
def diffusion(area,ac) : # 확산시키는 함수
    temp = [[0 for i in range(C)] for j in range(R)]
    temp[ac[0][0]][ac[0][1]] = -1
    temp[ac[1][0]][ac[1][1]] = -1
    for i in range(R) : 
        for j in range(C) : 
            if area[i][j] > 0 : 
                cnt = 0
                for d in range(4) : 
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<R and 0<=ny<C and area[nx][ny] != -1 :
                        temp[nx][ny] += area[i][j] // 5
                        cnt += 1
                temp[i][j] += area[i][j] - (area[i][j]//5*cnt)
    return temp
def air(x,y,dir) : # 환기시키는 함수
    temp = copy.deepcopy(area)
    cx,cy = x, y-1
    area[x][y] = 0
    for i in range(4) : 
        while True : 
            nx = x + dx[dir[i]]
            ny = y + dy[dir[i]]
            if nx == cx and ny == cy :
                return
            if 0<=nx<R and 0<=ny<C : 
                area[nx][ny] = temp[x][y]
            else : 
                break
            x,y = nx,ny

dx = [1,-1,0,0]
dy = [0,0,-1,1]
R,C,T = map(int,sys.stdin.readline().rstrip().split(' '))
area = []
for _ in range(R) : 
    area.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
ac = []
for i in range(R) : 
    for j in range(C) : 
        if area[i][j] == -1 : 
            ac.append([i,j])
for _ in range(T) : 
    area = diffusion(area,ac)
    air(ac[0][0],ac[0][1]+1,[3,1,2,0])
    air(ac[1][0],ac[1][1]+1,[3,0,2,1])
answer = 0
for i in range(R) : 
    for j in range(C) : 
        if area[i][j] > 0 :
            answer += area[i][j]
print(answer)