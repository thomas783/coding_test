n,k = map(int,input().split())
dp = [[0 for _ in range(max(n,k)+1)] for _ in range(max(n,k)+1)] # 메모리 최소화하기 위해 필요한 만큼만 리스트 만들어줌
for i in range(max(n,k)+1) : 
    dp[0][i] = 1 # 0을 k개로 나누어서 표현할 수 있는 개수는 1개
    dp[i][1] = 1 # n을 1개로 나누어서 표현할 수 있는 개수는 1개 
for i in range(1,n+1) : 
    for j in range(2,k+1) : 
        a,b = i,j
        while a >= 0 : # n을 k개로 나누어서 표현하는 경우 = n~0을 k-1개로 표현할 수 있는 경우의 합과 같음
            dp[i][j] += dp[a][b-1]
            a -= 1
            if dp[i][j] > 1000000000 : 
                dp[i][j] -= 1000000000
ans = dp[n][k]
print(ans)