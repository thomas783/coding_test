# 동전 0

import sys

input = sys.stdin.readline
n,k = map(int,input().split())
coin = []
for _ in range(n) : 
    coin.append(int(input()))
ans = 0
curr = n-1
while k>0 : 
    if k // coin[curr] > 0 : 
        ans += k // coin[curr]
        k -= (k // coin[curr]) * coin[curr]
    else : 
        curr -= 1
print(ans)