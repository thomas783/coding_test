import sys
sys.setrecursionlimit(10000)
n = int(input())
table = []
for _ in range(n) : 
    table.append(list(map(int,sys.stdin.readline().split())))
dx = [1,0]
dy = [0,1]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n) : 
    for j in range(n) : 
        if table[i][j] == 0 : # 0일 때 멈추기
            continue
        if dp[i][j] != 0 : 
            for d in range(2) : # 오른쪽 또는 아래로 보낼 수 있나 확인
                nx = i + dx[d] * table[i][j]
                ny = j + dy[d] * table[i][j]
                if 0<= nx < n and 0<= ny < n : 
                    # 가능하다면 경우의 수 합치기
                    dp[nx][ny] += dp[i][j]
print(dp[n-1][n-1])