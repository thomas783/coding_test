# 새로운 게임2

import sys

def go(y,x,d,idx,h,cnt) : 
    global maxi
    if cnt != 2 : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<n and 0<=nx<n :
            # 가려는 칸이 흰칸이나 빨강인 경우
            if table[ny][nx] == 0 or table[ny][nx] == 1 : 
                tmp = chess[y][x][idx:]
                chess[y][x] = chess[y][x][:idx]
                if table[ny][nx] == 1 : 
                    tmp = tmp[::-1]
                chess[ny][nx] += tmp
                for i in range(len(chess[ny][nx])) :
                    horse[chess[ny][nx][i]][0],horse[chess[ny][nx][i]][1] = ny, nx
                    horse[chess[ny][nx][i]][3] = i
                maxi = max(maxi,len(chess[ny][nx]))
                return
        # 가려는 칸이 파랑인 경우 혹은 갈 수 없는 경우
        d = dic[d]
        horse[h][2] = dic[horse[h][2]]
        go(y,x,d,idx,h,cnt+1)
    else : 
        horse[h][2] = dic[horse[h][2]]

input = sys.stdin.readline
n, k = map(int,input().split())
table = []
for _ in range(n) : 
    table.append(list(map(int,input().split())))
horse = []
for _ in range(k) : 
    i,j,l = map(int,input().split())
    horse.append([i-1,j-1,l-1,0])
chess = [[[] for _ in range(n)] for _ in range(n)]
for h in range(k) : 
    i,j,d,_ = horse[h]
    chess[i][j].append(h)
cnt = 0
dy = [0,0,-1,1]
dx = [1,-1,0,0]
dic = {0:1,1:0,2:3,3:2}
maxi = 0
while True : 
    cnt += 1
    for h in range(k) : 
        y,x,d,idx = horse[h]
        go(y,x,d,idx,h,0)
    if maxi >= 4 or cnt > 1000 : 
        break
if cnt > 1000 : 
    print(-1)
else : 
    print(cnt)