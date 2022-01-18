# 기타리스트

import sys

input = sys.stdin.readline
n,curr_vol,target = map(int,input().split())
v = list(map(int,input().split()))
dp = [[False for _ in range(target+1)] for _ in range(n+1)]
dp[0][curr_vol] = True
# dp[i][j]는 i번째 곡에서 가능한 볼륨 j를 boolean으로 담음.
for i in range(n) : 
    for j in range(target+1) : 
        if dp[i][j] :
            if 0<=j + v[i]<=target : 
                dp[i+1][j+v[i]] = True
            if 0<=j - v[i]<=target : 
                dp[i+1][j-v[i]] = True
ans = -1 
for j in range(target+1) : 
    if dp[-1][j] : 
        ans = max(ans,j)
print(ans)