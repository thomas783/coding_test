# 청소년 상어

import sys
import copy
def move_fish(area) : 
    temp_area = copy.deepcopy(area)
    dx = [0,-1,-1,0,1,1,1,0,-1]
    dy = [0,0,-1,-1,-1,0,1,1,1]
    dic = {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:1} # 반시계
    num = 1
    while num < 17 :
        flag = False
        for i in range(4) : 
            for j in range(4) :
                if temp_area[i][j] != [] : 
                    if temp_area[i][j][0] == num : 
                        dir = temp_area[i][j][1]
                        nx = dx[dir] + i
                        ny = dy[dir] + j
                        while True : # 출발 가능한 방향 찾기
                            if nx<0 or nx>3 or ny<0 or ny>3 or temp_area[nx][ny] == 'shark' : 
                                temp_area[i][j][1] = dic[temp_area[i][j][1]]
                                dir = temp_area[i][j][1]
                                nx = dx[dir] + i
                                ny = dy[dir] + j
                            else : 
                                break
                        temp_area[nx][ny],temp_area[i][j] = temp_area[i][j],temp_area[nx][ny]
                        num += 1
                        flag = True
        if not flag : 
            num += 1
    return temp_area 

def dfs(area,temp_answer,shark_dir) : 
    global answer
    area = move_fish(area)
    dx = [0,-1,-1,0,1,1,1,0,-1]
    dy = [0,0,-1,-1,-1,0,1,1,1]
    dic = {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:1}
    for i in range(4) : 
        for j in range(4) : 
            if area[i][j] == 'shark' : 
                area[i][j] = []
                for k in range(1,4) : 
                    nx = dx[shark_dir]*k + i
                    ny = dy[shark_dir]*k + j
                    if 0<=nx<4 and 0<=ny<4 and area[nx][ny] != [] : 
                        temp = area[nx][ny]
                        temp_shark_dir = shark_dir
                        temp_answer += temp[0]
                        shark_dir = temp[1]
                        area[nx][ny] = 'shark'
                        dfs(area,temp_answer,shark_dir)
                        area[nx][ny] = temp
                        shark_dir = temp_shark_dir
                        temp_answer -= temp[0]
                    answer = max(answer,temp_answer)

input = sys.stdin.readline
area = [[] for _ in range(4)]
for i in range(4) : 
    temp = list(map(int,input().split()))
    n = 0
    temp_li = []
    for t in temp : 
        if n % 2 == 0 : 
            temp_li.append(t)
            n += 1
        else : 
            temp_li.append(t)
            area[i].append(temp_li)
            temp_li = []
            n += 1
answer = 0
temp_answer = 0
answer += area[0][0][0]
temp_answer += area[0][0][0]
shark_dir = area[0][0][1]
area[0][0] = 'shark'
dfs(area,temp_answer,shark_dir)
print(answer)