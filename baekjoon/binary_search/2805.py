# 나무 자르기

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
li = list(map(int,input().split()))
li = sorted(li,reverse=True)
start,end = 0,1000000000
ans = 0
while start <= end : 
    mid = (start+end) // 2
    curr = 0
    for i in li :
        if i-mid > 0 : 
            curr += i-mid
        else : 
            break
    if curr >= m : 
        ans = mid
        start = mid + 1
    else : 
        end = mid - 1
print(ans)