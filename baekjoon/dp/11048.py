# 이동하기

N,M = map(int,input().split())
maze = []
for i in range(N) : 
    maze.append(list(map(int,input().split())))
dp = [[0 for _ in range(M)] for __ in range(N)]
dp[0][0] += maze[0][0]
for i in range(N) : 
    for j in range(M) : 
        if 0<= i+1 < N :
            if j+1 < M :
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + maze[i+1][j+1])
            dp[i+1][j] = max(dp[i+1][j],dp[i][j] + maze[i+1][j])
        if j+1<M : 
            dp[i][j+1] = max(dp[i][j+1],dp[i][j] + maze[i][j+1])
print(dp[N-1][M-1])