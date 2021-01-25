# 뱀

import sys
N = int(input())
K = int(input())
apple = []
for _ in range(K) : 
    i,j = map(int,sys.stdin.readline().rstrip().split(' '))
    apple.append([i-1,j-1])
L = int(input())
tilt = dict()
for _ in range(L) :
    i,j = map(str,sys.stdin.readline().rstrip().split(' '))
    tilt[int(i)] = j
maps = [[0 for _ in range(N)] for _ in range(N)]
maps[0][0] = 1
for i,j in apple : 
    maps[i][j] = 'A'

dir = [[0,1],[1,0],[0,-1],[-1,0]]
cur_dir = 0
cur_idx = [0,0]
last_idx = [[0,0]]
time = 0
while True : 
    if time in tilt.keys() : # 방향 전환
        if tilt[time] == 'D' : 
            cur_dir += 1
            if cur_dir == 4 : 
                cur_dir = 0
        else : 
            cur_dir -= 1
            if cur_dir == -1 : 
                cur_dir = 3
    time += 1
    next_x = cur_idx[0] + dir[cur_dir][0]
    next_y = cur_idx[1] + dir[cur_dir][1]
    if 0<=next_x<N and 0<=next_y<N :
        last_idx.append([next_x,next_y]) # 지나온길 저장
        cur_idx = [next_x,next_y]
        if maps[next_x][next_y] == 'A' : 
            maps[next_x][next_y] = 1
        elif maps[next_x][next_y] == 0 :  
            maps[next_x][next_y] = 1
            temp = last_idx.pop(0)
            maps[temp[0]][temp[1]] = 0
        else : # 자기 자신과 만났을 경우
            print(time)
            break
    else : 
        print(time)
        break