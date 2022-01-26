# 새로운 게임

import sys

def go(y,x,d,h,cnt) : 
    global maxi
    if cnt != 2 : 
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<n and 0<=nx<n :
            # 가려는 칸이 흰칸이나 빨강인 경우
            if table[ny][nx] == 0 or table[ny][nx] == 1 : 
                for i in chess[y][x] : 
                    horse[i][0],horse[i][1] = ny,nx
                if table[ny][nx] == 1 :
                    chess[y][x] = chess[y][x][::-1] 
                chess[ny][nx] += chess[y][x]
                maxi = max(maxi,len(chess[ny][nx]))
                chess[y][x] = []
                return
        # 가려는 칸이 파랑인 경우 혹은 갈 수 없는 경우
        d = dic[d]
        horse[h][2] = dic[horse[h][2]]
        go(y,x,d,h,cnt+1)
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
    horse.append([i-1,j-1,l-1])
chess = [[[] for _ in range(n)] for _ in range(n)]
for h in range(k) : 
    i,j,d = horse[h]
    chess[i][j].append(h)
cnt = 0
dy = [0,0,-1,1]
dx = [1,-1,0,0]
dic = {0:1,1:0,2:3,3:2}
maxi = 0
while True : 
    cnt += 1
    for h in range(k) : 
        y,x,d = horse[h]
        # 해당 말이 가장 아래 있는 말이라면
        if chess[y][x][0] == h : 
            go(y,x,d,h,0)
    if maxi >= 4 or cnt > 1000 : 
        break
if cnt > 1000 : 
    print(-1)
else : 
    print(cnt)