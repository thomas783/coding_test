# 동전 2

import sys
n,k = map(int,input().split())
coin = []
for _ in range(n) : 
    coin.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in coin : 
    for i in range(1,k+1) : 
        if i-c == 0 : 
            dp[i] = 1
        elif i-c > 0 : 
            if dp[i-c] != 0 and dp[i] == 0 : 
                dp[i] = dp[i-c] + 1
            elif dp[i-c] != 0 and dp[i] != 0 : 
                dp[i] = min(dp[i],dp[i-c]+1)
if dp[k] == 0 : 
    print(-1)
else :  
    print(dp[k])