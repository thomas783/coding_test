# 파일 합치기

import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t) : 
    k = int(input())
    li = list(map(int,input().split()))
    # dp[i][j]는 i~j까지의 최소값
    dp = [[0 for _ in range(k)] for _ in range(k)]
    # 옆의 두개씩 합친값을 계산하고
    # 어짜피 마지막에 해당 길이 만큼씩의 합을 구해야하니 미리 구함.
    for i in range(k-1) : 
        dp[i][i+1] = li[i] + li[i+1]
        for j in range(i+2,k) : 
            dp[i][j] = dp[i][j-1] + li[j]
    # (1,3),(2,2),(3,1) 이런식으로 쪼개진 애들끼리 비교해서 최소 찾기
    for d in range(2,k) : 
        for i in range(k-d) : 
            j = i+d
            mini = [dp[i][m] + dp[m+1][j] for m in range(i,j)]
            dp[i][j] += min(mini)
    print(dp[0][k-1])