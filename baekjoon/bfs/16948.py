# 데스나이트

from collections import deque
import sys
N = int(input())
r1,c1,r2,c2 =  map(int,input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
cnt = 0
q = deque()
q.append([r1,c1,cnt])
ans = sys.maxsize
visited = [[r1,c1]]
while q : 
    x,y,cnt = q.popleft()
    for d in range(6) : 
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<N and [nx,ny] not in visited : 
            if nx == r2 and ny == c2 : 
                ans = min(ans,cnt+1)
            else : 
                q.append([nx,ny,cnt+1])
                visited.append([nx,ny])
if ans == sys.maxsize : 
    print(-1)
else : 
    print(ans)