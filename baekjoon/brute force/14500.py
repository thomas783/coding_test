# 테트로미노

import sys
N,M = map(int,sys.stdin.readline().rstrip().split(' '))
maps = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]

polios = []
dx = [0,0,1]
dy = [1,-1,0]
queue = [[[0,0]],[[0,1]],[[0,2]]] # x,y 좌표와 길이
while queue : 
    temp = queue.pop(0)
    for dir in range(3) : 
        next_x = temp[-1][0] + dx[dir]
        next_y = temp[-1][1] + dy[dir]
        if [next_x,next_y] not in temp and next_x >= 0 and next_y >= 0: 
            if len(temp+[[next_x,next_y]]) == 4 : 
                polios.append(temp+[[next_x,next_y]])
            else : 
                queue.append(temp+[[next_x,next_y]])
        else : 
            continue
new_polios = []
for p in polios : 
    a = 100 
    b = 100
    for i,j in p : 
        a = min(a,i)
        b = min(b,j)
    temp = sorted([[i-a,j-b] for i,j in p],key = lambda x : (x[0],x[1]))
    if temp not in new_polios : 
        new_polios.append(temp)
middle = [[[0,0],[0,1],[0,2],[1,1]],
[[0,1],[1,0],[1,1],[1,2]],
[[0,0],[1,0],[2,0],[1,1]],
[[0,1],[1,0],[1,1],[2,1]]] # 볼록할 철 자 모양 4개 추가
new_polios += middle 
answer = 0
for p in new_polios :      
    for i in range(N) : 
        for j in range(M) : 
            temp = 0
            for x,y in p : 
                if 0<=x+i<N and 0<=y+j<M : 
                    temp += maps[x+i][y+j]
            answer = max(answer,temp)
print(answer)




