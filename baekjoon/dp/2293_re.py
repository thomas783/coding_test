# 동전 1

n,k = map(int,input().split())
coin = []
for _ in range(n) : 
    coin.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in coin : 
    for i in range(1,k+1) : 
        if i-c >= 0 : 
            dp[i] += dp[i-c]
print(dp[k])