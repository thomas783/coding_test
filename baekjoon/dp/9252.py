# LCS 2

import sys

li1 = input().rstrip()
li2 = input().rstrip()
dp = [['' for _ in range(len(li2)+1)] for _ in range(len(li1)+1)]
for i in range(1,len(li1)+1) : 
    for j in range(1,len(li2)+1) : 
        if i == 0 and j == 0 : 
            dp[i][j] = ''
        elif li1[i-1] == li2[j-1] :
            dp[i][j] = dp[i-1][j-1] + li1[i-1]
        else : 
            if len(dp[i-1][j]) >= len(dp[i][j-1]) : 
                dp[i][j] = dp[i-1][j]
            else : 
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
if dp[-1][-1] : 
    print(dp[-1][-1])