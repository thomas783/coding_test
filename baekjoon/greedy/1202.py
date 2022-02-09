# 보석 도둑

import sys
import heapq

input = sys.stdin.readline
n,k = map(int,input().split())
mv = [list(map(int,input().split())) for _ in range(n)]
c = [int(input()) for _ in range(k)]
mv.sort()
c.sort()
ans = 0
tmp = []
for c_weight in c : 
    while mv and c_weight >= mv[0][0] : 
        # max haep
        heapq.heappush(tmp,-mv[0][1])
        heapq.heappop(mv)
    if tmp : 
        ans += heapq.heappop(tmp)
    elif not c :
        break
print(-ans)