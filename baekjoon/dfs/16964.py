# DFS 스페셜 저지

import sys

def dfs(node,lv) : 
    if visited[node] == 1 :
        return 0
    visited[node] = 1
    size = 1
    level[node] = lv
    for i in range(len(table[node])) :
        next = table[node][i]
        size += dfs(next,lv+1)
    tsize[node] = size
    return size

input = sys.stdin.readline
N = int(input())
table = [[] for _ in range(N+1)]
for _ in range(N-1) : 
    x,y = map(int,input().split())
    table[x].append(y)
    table[y].append(x)
li = list(map(int,input().split()))
visited = [0 for _ in range(N+1)]
level = [0 for _ in range(N+1)]
tsize = [0 for _ in range(N+1)]
if li[0] != 1 : 
    print(0)
    sys.exit(0)
else : 
    dfs(1,0)
    for i in range(1,N) : 
        node = li[i]
        if tsize[node] == 1 or i + tsize[node] >= N : 
            continue
        next = li[i+tsize[node]]
        if level[next] > level[node] :
            print(0)
            sys.exit(0)
    print(1)