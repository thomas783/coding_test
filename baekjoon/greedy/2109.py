# 순회강연

import sys
import heapq

input = sys.stdin.readline
n = int(input())
pd = [list(map(int,input().split())) for _ in range(n)]
pd = sorted(pd,key=lambda x : (x[1],-x[0]))[::-1]
ans = []
while pd :
    p,d = pd.pop()
    if len(ans) >= d and ans[0] < p: 
        heapq.heappop(ans)
        heapq.heappush(ans,p)
    elif len(ans) < d : 
        heapq.heappush(ans,p)
    elif len(ans) >= d and ans[0] >= p : 
        continue
print(sum(ans))