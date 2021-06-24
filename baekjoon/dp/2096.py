import sys

n = int(input())
table = []
dp = list(map(int,input().split())) * 2
for _ in range(1,n) : # dp[0] ~ dp[2]는 최대점수, dp[3] ~ dp[5]는 최소점수
    table = list(map(int,input().split())) # 보통은 리스트에 담아서 계산하겠지만 메모리가 4mb로 상당히 적어서 메모리 사용량을 최소로 한다.
    dp[0],dp[1],dp[2] = max(dp[0],dp[1]) + table[0], max(dp[0],dp[1],dp[2]) + table[1], max(dp[1],dp[2]) + table[2]
    dp[3],dp[4],dp[5] = min(dp[3],dp[4]) + table[0], min(dp[3],dp[4],dp[5]) + table[1], min(dp[4],dp[5]) + table[2]
print(max(dp[:3]),min(dp[3:]))