# 낚시왕

import sys
def move(shark) : 
    dic = dict({1:2,2:1,3:4,4:3}) # 움직일 방향전환용
    temp = []
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for r,c,s,d,z in shark : 
        for _ in range(s) : 
            nx = r+dx[d-1]
            ny = c+dy[d-1]
            if 0<=nx<R and 0<=ny<C :
                r,c = nx, ny
            else : 
                d = dic[d]
                r += dx[d-1]
                c += dy[d-1]
        temp.append([r,c,s,d,z])
    return temp

        
R,C,M = map(int,sys.stdin.readline().rstrip().split(' '))
shark = []
for _ in range(M) : 
    r,c,s,d,z = map(int,sys.stdin.readline().rstrip().split(' '))
    shark.append([r-1,c-1,s,d,z])
answer = 0
for _ in range(C) :
    # 낚시하기
    area = [[0 for i in range(C)] for j in range(R)]
    temp = []
    for r,c,s,d,z in shark : 
        area[r][c] = [s,d,z]
    for i in range(R) : 
        if area[i][_] != 0 : 
            answer += area[i][_][2]
            area[i][_] = 0
            break
    for i in range(R) : 
        for j in range(C) : 
            if area[i][j] != 0 :
                temp.append([i,j]+area[i][j])
    shark = temp
    # 상어 움직임
    shark = move(shark)
    area = [[0 for i in range(C)] for j in range(R)]
    for r,c,s,d,z in shark : 
        if area[r][c] == 0 : 
            area[r][c] = [s,d,z]
        else : # 상어끼리 먹는경우
            if area[r][c][2] < z : 
                area[r][c] = [s,d,z]
    temp = []
    for i in range(R) : 
        for j in range(C) : 
            if area[i][j] != 0 : 
                temp.append([i,j] + area[i][j])
    shark = temp
print(answer)