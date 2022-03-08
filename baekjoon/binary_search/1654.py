# 랜선 자르기

import sys

input = sys.stdin.readline
k,n = map(int,input().split())
li = [int(input()) for _ in range(k)]
start,end = 1,max(li)
ans = 1
curr = sum(li)
while start <= end : 
    mid = (start+end)//2
    curr = sum([i//mid for i in li])
    if curr >= n : 
        ans = mid
        start = mid + 1
    else : 
        end = mid - 1
print(ans)