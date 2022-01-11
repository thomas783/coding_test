# 스타트링크

import sys
from collections import deque

n,curr,target,u,d = map(int,input().split())
if curr == target : 
    print(0)
    sys.exit(0)
deq = deque()
deq.append([curr,0])
visited = [False for _ in range(n+1)]
visited[curr] = True
ans = sys.maxsize
while deq : 
    curr, num = deq.popleft()
    for a in [u,-d] : 
        ncurr = curr + a
        if 1<= ncurr <= n and not visited[ncurr] :
            if ncurr == target : 
                ans = min(ans,num+1)
            else : 
                deq.append([ncurr,num+1])
                visited[ncurr] = True
if ans == sys.maxsize : 
    print('use the stairs')
else : 
    print(ans)