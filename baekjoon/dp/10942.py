# 팰린드롬?

import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
m = int(input())
q = []
for _ in range(m) : 
    i,j = map(int,input().split())
    q.append([i-1,j-1])
dp = [[0 for _ in range(n)] for _ in range(n)]
# 길이가 1이면 무조건 팰린드롬
for i in range(n) : 
    for j in range(n) : 
        if i == j :
            dp[i][j] = 1
# 길이가 2일때 같은 수라면 팰린드롬
for i in range(n-1) : 
    if li[i] == li[i+1] : 
        dp[i][i+1] = 1
# 길이가 3일때 1번과 3번이 같은 수라면 팰린드롬
for i in range(n-2) : 
    if li[i] == li[i+2] : 
        dp[i][i+2] = 1
# 길이가 4이상 일 때
for i in range(3,n-1) : # 길이
    for j in range(0,n-i) : # 시작점
        if dp[j+1][i+j-1] and li[j] == li[i+j] : 
            dp[j][i+j] = 1
# 전체 확인
if dp[1][-2] and li[0] == li[-1] : 
    dp[0][-1] = 1
for i,j in q : 
    print(dp[i][j])