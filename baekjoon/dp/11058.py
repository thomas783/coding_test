# 크리보드

# 3개전 것을 두배하는 경우와
# ctrlc,ctrlv를 여러번 누르는 경우의 최대 값 계산
import sys
n = int(input())
dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5
for i in range(6,n+1) : 
    dp[i] = max([dp[i-3]*2] + [dp[i-k-2]*(k+1) for k in range(1,i)])
print(dp[n])