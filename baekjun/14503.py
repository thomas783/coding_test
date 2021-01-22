# 로봇 청소기

import sys
def clean(room,x,y,dir,visited) : 
    dx = [0,-1,0,1] # 왼쪽 탐색할 방향
    dy = [-1,0,1,0]
    bx = [1,0,-1,0] # 후진 할 방향
    by = [0,-1,0,1]
    global answer
    if room[x][y] == 0 : # 1번 조건
        if [x,y] not in visited : 
            visited.append([x,y])
            answer += 1
    cnt = 0
    while cnt < 4 : 
        cnt += 1
        if 0<=x+dx[dir]<N and 0<=y+dy[dir]<M and room[x+dx[dir]][y+dy[dir]] == 0 and [x+dx[dir],y+dy[dir]] not in visited : # 2.a의 조건
            x = x+dx[dir]
            y = y+dy[dir]
            if dir == 0 : 
                dir = 3 
            else : 
                dir -= 1
            visited.append([x,y])
            clean(room,x,y,dir,visited)
            return
        else : 
            if dir == 0 : # 2.b의 조건
                dir = 3 
            else : 
                dir -= 1
    if room[x+bx[dir]][y+by[dir]] == 1 : # 2.d의 조건
        return 
    else : # 2.c의 조건
        clean(room,x+bx[dir],y+by[dir],dir,visited)
        return
    
N,M = map(int,sys.stdin.readline().rstrip().split(' '))
x,y,dir = map(int,sys.stdin.readline().rstrip().split(' '))
room = []
visited = []
answer = 0
for _ in range(N) : 
    room.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
clean(room,x,y,dir,visited)
print(answer)
print(visited,len(visited))