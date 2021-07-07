# 공통 부분 문자열
# 시간초과 때문에 pypy3로 품 

import sys
answer = 0
str1,str2 = input(),input()
dp = [[0 for _ in range(len(str1)+1)] for __ in range(len(str2)+1)]
for i in range(1,len(str2)+1) : 
    for j in range(1,len(str1)+1) : 
        if str2[i-1] == str1[j-1] : 
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer,dp[i][j])
print(answer)