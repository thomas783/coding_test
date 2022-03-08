# 버블 소트

import sys
n = int(input())
li = [[int(input()),i] for i in range(n)]
new = sorted(li)
ans = 0
for i in range(n) : 
    ans = max(new[i][1]-i+1,ans)
print(ans)