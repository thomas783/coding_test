# 공유기 설치

import sys

input = sys.stdin.readline
n,c = map(int,input().split())
li = [int(input()) for _ in range(n)]
li = sorted(li)
start,end = 0,1000000000
ans = 0
while start <= end : 
    mid = (start+end) // 2
    curr = li[0]
    cnt = 1
    for i in range(1,len(li)) :
        if li[i] - curr >= mid : 
            cnt += 1
            curr = li[i]
    if cnt >= c : 
        start = mid + 1
        ans = mid
    else : 
        end = mid - 1
print(ans)