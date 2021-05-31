import sys

input = sys.stdin.readline
N,M = list(map(int,input().split()))
table = []
for _ in range(N) : 
    table.append(list(map(int,input().split())))
move = []
for _ in range(M) : 
    x,y = list(map(int,input().split()))
    move.append([x-1,y])
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
for i in range(M) :
    # 1번
    d,s = move[i] 
    temp_cloud = []
    for x,y in cloud :
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        temp_cloud.append([nx,ny])
    # 2번
    visited = [[False] * N for _ in range(N)]
    for r,c in temp_cloud : 
        table[r][c] += 1
        visited[r][c] = True
    # 3번
    cloud = []
    # 4번
    for r,c in temp_cloud : 
        for dir in [1,3,5,7] : 
            nx = r + dx[dir]
            ny = c + dy[dir]
            if 0<=nx<N and 0<=ny<N and table[nx][ny] > 0 : 
                table[r][c] += 1
    # 5번
    for x in range(N) : 
        for y in range(N) : 
            if table[x][y] >= 2 and visited[x][y] == False : 
                cloud.append([x,y])
                table[x][y] -= 2
answer = 0
for i in range(N) : 
    for j in range(N) : 
        answer += table[i][j]
print(answer)