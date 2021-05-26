import sys
N = int(input())
table = []
for _ in range(N) : 
    table.append(list(map(int,sys.stdin.readline().split())))
start = [N//2,N//2]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
move = []
flag = True
for i in range(1,N) : 
    if flag : 
        move += [0] * i
        move += [1] * i
        flag = False
    else : 
        move += [2] * i
        move += [3] * i
        flag = True
move += [0] * (N-1)
tor_dx = [[-2,-1,-1,-1,0,0,1,1,1,2],[0,1,0,-1,2,1,1,0,-1,0],[2,1,1,1,0,0,-1,-1,-1,-2],[0,-1,0,1,-2,-1,-1,0,1,0]]
tor_dy = [[0,-1,0,1,-2,-1,-1,0,1,0],[-2,-1,-1,-1,0,0,1,1,1,2],[0,1,0,-1,2,1,1,0,-1,0],[2,1,1,1,0,0,-1,-1,-1,-2]]
tor_val = [0.02,0.1,0.07,0.01,0.05,0,0.1,0.07,0.01,0.02]
answer = 0
for d in move : 
    nx = start[0] + dx[d]
    ny = start[1] + dy[d]
    start = [nx,ny]
    alpha = table[nx][ny]
    if alpha != 0 : 
        for x,y,val in zip(tor_dx[d],tor_dy[d],tor_val) : 
            if 0<=nx+x<N and 0<=ny+y<N :
                table[nx+x][ny+y] += int(table[nx][ny] * val)
                alpha -= int(table[nx][ny] * val)
            else :
                answer += int(table[nx][ny] * val)
                alpha -= int(table[nx][ny] * val)
        if 0<=nx+tor_dx[d][5]<N and 0<=ny+tor_dy[d][5]<N :
            table[nx+tor_dx[d][5]][ny+tor_dy[d][5]] += alpha
        else : 
            answer += alpha
    table[start[0]][start[1]] = 0
print(answer)