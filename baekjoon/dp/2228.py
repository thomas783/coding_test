# 구간 나누기

import sys
INF = sys.maxsize
N,M = map(int,input().split())
li = []
for _ in range(N) : 
    li.append(int(input()))
li = [0] + li
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
check = [[False for _ in range(M+1)] for _ in range(N+1)]
# dp[N][M] = dp[N-1][M]
# dp[N][M] = max(dp[k-2][M-1] + sum(li[k:i]))
def find(N,M) :
    if M == 0 : 
        return 0
    if N < M*2-1 :
        return -INF
    if check[N][M] : 
        return dp[N][M]
    check[N][M] = True
    dp[N][M] = find(N-1,M) # 마지막 수가 포함되지 않는 경우
    for k in range(N,0,-1) : # 마지막 수가 포함되는 경우
        dp[N][M] = max(find(k-2,M-1) + sum(li[k:N+1]),dp[N][M])
    return dp[N][M]
print(find(N,M))