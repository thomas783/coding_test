# 인구 이동

import sys
from collections import defaultdict,deque
def bfs(cur) : # bfs를 통해 연합을 찾아낸다.
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [cur]
    deq = deque()
    deq.append(cur)
    while deq : 
        x,y = deq.popleft()
        val = area[x][y]
        for i in range(4) : 
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<=next_x<N and 0<=next_y<N and visited_all[next_x][next_y] == 0 and L<=abs(area[next_x][next_y]-val)<=R : 
                visited_all[next_x][next_y] = 1
                deq.append([next_x,next_y])
                visited.append([next_x,next_y])
    return visited

N,L,R = map(int,sys.stdin.readline().rstrip().split(' '))
area = []
for _ in range(N) :
    area.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
answer = 0
while True : 
    visited_all = [[0]*N for i in range(N)]
    cur_num = 0 
    isTrue = False
    for i in range(N) : 
        for j in range(N) : 
            if visited_all[i][j] == 0 : 
                visited_all[i][j] = 1
            temp = bfs([i,j])
            if len(temp) > 1 : 
                isTrue = True
                num = sum([area[x][y] for x,y in temp])//len(temp)
                for x,y in temp : 
                    area[x][y] = num
    if not isTrue : 
        break
    answer += 1
print(answer)