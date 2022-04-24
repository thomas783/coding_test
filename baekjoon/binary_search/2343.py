# 기타 레슨

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
lesson = list(map(int,input().split()))
start,end = max(lesson),sum(lesson)
ans = sys.maxsize
while start <= end : 
    mid = (start + end)//2
    idx,curr,blueray = 0,0,1
    while idx < n : 
        if curr + lesson[idx] > mid : 
            blueray += 1
            curr = lesson[idx]
            idx += 1
        else : 
            curr += lesson[idx]
            idx += 1
    if blueray <= m : 
        ans = min(ans,mid)
        end = mid - 1
    else : 
        start = mid + 1
print(ans)