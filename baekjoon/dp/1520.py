import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
m,n = map(int,input().split())
table = []
for _ in range(m) : 
    table.append(list(map(int,input().split())))
ans = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y) : 
    if x == 0 and y == 0 : 
        return 1
    if dp[x][y] == -1 : 
        dp[x][y] = 0
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<= ny < n : 
                if table[x][y] < table[nx][ny] :
                    dp[x][y] += dfs(nx,ny)
    return dp[x][y]
dp = [[-1] * n for i in range(m)]
print(dfs(m-1,n-1))