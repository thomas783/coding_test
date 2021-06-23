n = int(input())
dp = [[0] * 3 for _ in range(n+1)]
for i in range(3) : 
    dp[1][i] = 1
for i in range(2,n+1) : 
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901 # 왼쪽에 사자가 있는 경우
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901 # 오른쪽에 사자가 있는 경우
    dp[i][2] = sum(dp[i-1]) % 9901 # 어느쪽에도 없는 경우
print(sum(dp[n])%9901)