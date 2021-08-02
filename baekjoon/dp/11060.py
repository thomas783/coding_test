# 점프 점프

import sys
N = int(input())
li = list(map(int,input().split()))
dp = [sys.maxsize for _ in range(N)]
dp[0] = 0
for i in range(N) : 
    if li[i] > 0 : 
        for j in range(1,li[i]+1) : 
            if i + j < N :
                dp[i+j] = min(dp[i] + 1,dp[i+j])
if dp[-1] == sys.maxsize : 
    print(-1)
else : 
    print(dp[-1])