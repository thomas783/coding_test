# 드래곤 커브

import sys
dic = dict({0:1,1:2,2:3,3:0}) # 시계방향으로 돌리는 idx
def make_dragon(start,d,g) : 
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    idx = [d] # 다음으로 갈 방향 저장
    visited.append(start)
    cur = [start[0] + dx[d],start[1] + dy[d]]
    visited.append(cur)
    for _ in range(g) : 
        temp_idx = []
        for i in idx : 
            i = dic[i]
            next_x = cur[0] + dx[i]
            next_y = cur[1] + dy[i]
            cur = [next_x,next_y]
            visited.append(cur)
            temp_idx.append(i)
        idx = temp_idx[::-1] + idx

N = int(input())
visited = [] # 드래곤 커브가 포함되는 꼭지점들
for _ in range(N) : 
    y,x,d,g = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    start = [x,y]
    make_dragon(start,d,g)
answer = 0
for i in range(100) : 
    for j in range(100) : 
        if [i,j] in visited and [i+1,j] in visited and [i,j+1] in visited and [i+1,j+1] in visited :
            answer += 1
print(answer)