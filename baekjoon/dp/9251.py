# LCS(Longest Common Sequence)

import sys

li1 = input().rstrip()
li2 = input().rstrip()
dp = [[0 for _ in range(len(li2)+1)] for _ in range(len(li1)+1)]
for i in range(1,len(li1)+1) : 
    for j in range(1,len(li2)+1) : 
        if i == 0 and j == 0 : 
            dp[i][j] = 0
        elif li1[i-1] == li2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else : 
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])