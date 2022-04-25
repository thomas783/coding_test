# 구간 나누기 2

import sys

def divide(x) : 
    maxi=mini=li[0]
    cnt = 1
    for i in range(1,n) : 
        maxi = max(maxi,li[i])
        mini = min(mini,li[i])
        if maxi - mini > x : 
            cnt += 1
            maxi = li[i]
            mini = li[i]
    return cnt

input = sys.stdin.readline
n,m = map(int,input().split())
li = list(map(int,input().split()))
start,end = 0, max(li)
ans = 0
while start <= end : 
    mid = (start+end)//2
    if divide(mid) <= m : 
        end = mid - 1
        ans = mid
    else : 
        start = mid + 1
print(ans)