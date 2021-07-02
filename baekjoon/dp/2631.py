import sys
# 가장 큰 증가하는 수열을 찾아서 n에서 빼면 된다.

n = int(input())
li = []
for _ in range(n) : 
    li.append(int(input()))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1,n) : 
    temp = []
    for j in range(i) : 
        if li[i] > li[j] : 
            temp.append(dp[j])
    if temp == [] : 
        dp[i] = 1
    else : 
        dp[i] = max(temp) + 1
print(n - max(dp))