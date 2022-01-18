# 평번한 배낭

import sys

input = sys.stdin.readline
n,k = map(int,input().split())
bag = []
for _ in range(n) : 
    bag.append(list(map(int,input().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# 가방의 무게가 현재 물건보다 무게가 작다면 바로
# [이전 물건][같은 무게]로 바꿔준다.
# 아니라면 현재 물건의 가치+ [이전 물건][현재 가방무게-현재물건무게],
# [이전 물건][현재 가방 무게]의 최댓값을 구해준다.
for i in range(1,n+1) : 
    for j in range(1,k+1) : 
        curr_weight,curr_value = bag[i-1]
        if j < curr_weight : 
            dp[i][j] = dp[i-1][j]
        else : 
            dp[i][j] = max(curr_value+dp[i-1][j-curr_weight],dp[i-1][j])
print(dp[n][k])