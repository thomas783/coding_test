# 어른 상어 

import sys
def move_shark(new_area,N,M,K,shark,dir,move) : 
    excep = [] # 자신이 있던 곳으로 되돌아온 경우
    curr_loc = []
    for i in range(len(shark)) : 
        if shark[i] != 'dead' : 
            curr_loc.append(shark[i])
    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]
    for s in range(1,M+1) : 
        if shark[s] != 'dead' : 
            curr_dir = dir[s]
            pri = move[s][curr_dir-1]
            flag = False
            for i in pri : 
                nx = shark[s][0] + dx[i]
                ny = shark[s][1] + dy[i]
                if 0<=nx<N and 0<=ny<N and [nx,ny] not in curr_loc: # 빈칸으로 가는 경우
                    if new_area[nx][ny] == [0,0] : 
                        new_area[nx][ny] = [s,K]
                        new_area[shark[s][0]][shark[s][1]] = [s,K]
                        shark[s] = [nx,ny]
                        dir[s] = i 
                        flag = True
                        break
                    elif new_area[nx][ny][1] == K and [nx,ny] not in excep: # 다른 상어를 만나는 경우 
                        if s < new_area[nx][ny][0] : 
                            shark[new_area[nx][ny][0]] = 'dead'
                            new_area[nx][ny] = [s,K]
                            new_area[shark[s][0]][shark[s][1]] = [s,K]
                            shark[s] = [nx,ny]
                            dir[s] = i 
                            flag = True
                            break
                        else : 
                            new_area[shark[s][0]][shark[s][1]] = [s,K]
                            shark[s] = 'dead'
                            flag = True
                            break
            if not flag : 
                for i in pri : # 자기 자신으로 돌아가는 경우
                    nx = shark[s][0] + dx[i]
                    ny = shark[s][1] + dy[i]
                    if 0<=nx<N and 0<=ny<N and new_area[nx][ny][0] == s : 
                        new_area[nx][ny] = [s,K]
                        new_area[shark[s][0]][shark[s][1]] = [s,K]
                        shark[s] = [nx,ny]
                        dir[s] = i
                        excep.append([nx,ny])
                        break
    for i in range(N) : 
        for j in range(N) : 
            if 0<new_area[i][j][1]<=K :  
                new_area[i][j][1] -= 1
                if new_area[i][j][1] == 0 : 
                    new_area[i][j] = [0,0]
    for s in shark : 
        if s != 'dead' :
            new_area[s[0]][s[1]][1] += 1
            
input = sys.stdin.readline
N,M,K = list(map(int,input().split()))
area = []
for _ in range(N) :
    area.append(list(map(int,input().split())))
new_area = []
shark = [[0,0,0]]
for i in range(N) : 
    temp_li = []
    for j in range(N) : 
        if area[i][j] != 0 : 
            shark.append([area[i][j],i,j])
            temp_li.append([area[i][j],-1])
        else : 
            temp_li.append([0,0])
    new_area.append(temp_li)
shark = sorted(shark,key = lambda x : x[0])
shark = [[j,k] for i,j,k in shark]
shark[0] = 'dead'
dir = [0] + list(map(int,input().split()))
move = [[0]]
for _ in range(M) : 
    temp = []
    for i in range(4) : 
        temp.append(list(map(int,input().split())))
    move.append(temp)
flag = False
for time in range(1,1001) : 
    move_shark(new_area,N,M,K,shark,dir,move)
    alive = 0
    for i in range(len(shark)) : 
        if shark[i] != 'dead' : 
            alive += 1
    if alive == 1 : 
        flag = True
        print(time)
        break
if not flag : 
    print(-1)