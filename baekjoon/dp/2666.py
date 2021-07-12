# 벽장문의 이동

import sys

N = int(input())
a,b = map(int,input().split())
M = int(input())
queue = []
for _ in range(M) : 
    queue.append(int(input()))
dp = [[[-1 for _ in range(N+1)] for __ in range(N+1)] for ___ in range(M)]
def find(idx,a,b) : 
    if idx == M : # 예외처리
        return 0
    if dp[idx][a][b] != -1 : 
        return dp[idx][a][b]
    temp1 = find(idx+1,queue[idx],b) + abs(queue[idx] - a)
    temp2 = find(idx+1,a,queue[idx]) + abs(queue[idx] - b)
    dp[idx][a][b] = min(temp1,temp2)
    return dp[idx][a][b]
print(find(0,a,b))