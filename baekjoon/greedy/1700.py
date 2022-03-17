# 멀티탭 스케줄링

import sys

input = sys.stdin.readline
n,k = map(int,input().split())
li = list(map(int,input().split()))
plug = [0 for _ in range(n)]
ans = 0
for i in range(k) :
    if li[i] in plug : 
        continue
    if 0 in plug :
        idx = plug.index(0)
        plug[idx] = li[i]
        continue
    tmp = [-1 for _ in range(n)]
    cnt = k-1
    for j in li[i:] : 
        if j in plug and tmp[plug.index(j)] == -1 : 
            tmp[plug.index(j)] = cnt
            cnt -= 1
    for j in range(-1,k) : 
        if j in tmp : 
            plug[tmp.index(j)] = li[i]
            ans += 1
            break
print(ans)