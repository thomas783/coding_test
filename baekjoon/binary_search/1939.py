# 중량제한

import sys
from collections import deque

def bfs(start,end,mid) : 
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q : 
        curr = q.popleft()
        for i,cnt in table[curr] : 
            if cnt >=mid and i not in visited : 
                q.append(i)
                visited.add(i)
    return True if end in visited else False

input = sys.stdin.readline
n,m = map(int,input().split())
table = [[] for _ in range(n+1)]
for _ in range(m) : 
    i,j,k = map(int,input().split())
    table[i].append((j,k))
    table[j].append((i,k))
start,end = map(int,input().split())
left,right = 1,1000000000
ans = 0
while left <= right : 
    mid = (left+right)//2
    if bfs(start,end,mid) : 
        left = mid + 1
        ans = mid
    else : 
        right = mid - 1
print(ans)