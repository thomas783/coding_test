# ATM

import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int,input().split()))
p = sorted(p)
ans = [0 for _ in range(n)]
ans[0] = p[0]
for i in range(1,n) : 
    ans[i] = ans[i-1] + p[i]
print(sum(ans))