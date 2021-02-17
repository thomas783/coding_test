# 파도반 수열

import sys
N = int(input())
ans = [1,1,1,2,2,3,4,5,7,9]
for i in range(90) : 
    ans.append(ans[-1]+ans[-5])
for _ in range(N) : 
    val = int(input()) - 1
    print(ans[val])