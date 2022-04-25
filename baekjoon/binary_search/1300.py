# k번째 수

import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
start,end = 1,n**2
ans = 0
while start <= end : 
    mid = (start + end)//2
    tmp = 0
    for i in range(1,n+1) : 
        tmp += min(mid//i,n)
    if tmp < k : 
        start = mid + 1
    else : 
        ans = mid
        end = mid - 1
print(ans)