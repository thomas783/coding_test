# 주사위 굴리기

import sys, copy
M,N,x,y,K = map(int,sys.stdin.readline().rstrip().split(' '))
maps = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(M)]
moves = list(map(int,sys.stdin.readline().rstrip().split(' ')))
dice = [0 for _ in range(7)]
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
for i in range(K) :
    dir = moves[i]
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0<=nx<M or not 0<=ny<N : 
        continue
    if dir == 1 : # 동쪽으로 굴리는 경우
        dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
    elif dir == 2 : # 서쪽
        dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
    elif dir == 3 : # 북쪽
        dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]
    else : # 남쪽
        dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]
    if maps[nx][ny] == 0 :
        maps[nx][ny] = dice[6]
    else : 
        dice[6] = maps[nx][ny]
        maps[nx][ny] = 0
    x,y = nx,ny
    print(dice[1]) 