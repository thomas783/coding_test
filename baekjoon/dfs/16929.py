# Two Dots
from copy import deepcopy
def dfs(curr,start,visited) : 
    global ans
    if ans : 
        return
    x,y = curr
    for d in range(4) : 
        nx = x + dx[d]
        ny = y + dy[d]
        if ans : 
            return
        if 0<= nx < N and 0<= ny < M : 
            if table[x][y] == table[nx][ny] and [nx,ny] not in visited :
                visited.append([nx,ny])
                dfs([nx,ny],start,visited)
                visited.pop()
    if len(visited) >= 3 :
        temp_x,temp_y = visited[-1]
        if abs(temp_x-start[0]) + abs(temp_y-start[1]) == 1 :
            ans = True
            return True
    return False

N,M = map(int,input().split())
table = []
for _ in range(N) : 
    table += input().split()
ans = False
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(N) : 
    for j in range(M) : 
        dfs([i,j],[i,j],[[i,j]])
        if ans : 
            break
    if ans : 
        break
if ans : 
    print('Yes')
else : 
    print('No')