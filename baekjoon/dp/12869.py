# 뮤탈리스크

import sys
import itertools

# dp[i][j][k] = scv의 체력이 각각 i,j,k일 때 파괴할 수 있는 최소 횟수
def go(a,b,c) : 
    if a < 0 : 
        return go(0,b,c)
    if b < 0 : 
        return go(a,0,c)
    if c < 0 : 
        return go(a,b,0)
    if a == 0 and b == 0 and c == 0 : 
        return 0
    if dp[a][b][c] != -1 : 
        return dp[a][b][c]
    dp[a][b][c] = sys.maxsize
    for i in itertools.permutations([1,3,9]) : 
        dp[a][b][c] = min(dp[a][b][c],go(a-i[0],b-i[1],c-i[2]))
    dp[a][b][c] += 1
    return dp[a][b][c]
    
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
scv = [0,0,0]
for i in range(len(li)) : 
    scv[i] = li[i]
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
print(go(scv[0],scv[1],scv[2]))