# 나무 재테크

import sys
from collections import deque
input = sys.stdin.readline
n,m,k = map(int,input().split())
feed = [] # 매년 추가될 양분의 양
for _ in range(n) : 
    feed.append(list(map(int,input().split())))
fertilizer = [[5 for _ in range(n)] for __ in range(n)] # 각 칸에 담겨진 양분의 양
tree = [[deque() for _ in range(n)] for __ in range(n)] # 나무 정보
for _ in range(m) : 
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)
for _ in range(k) : 
    # 봄
    for i in range(n) : 
        for j in range(n) : 
            for t in range(len(tree[i][j])) : 
                if tree[i][j][t] <= fertilizer[i][j] : 
                    fertilizer[i][j] -= tree[i][j][t]
                    tree[i][j][t] += 1
                else : 
                    for _ in range(t,len(tree[i][j])) : # 여름
                        fertilizer[i][j] += tree[i][j].pop()//2
                    break
    # 가을
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for i in range(n) : 
        for j in range(n) : 
            for t in tree[i][j] : 
                if t % 5 == 0 : 
                    for d in range(8) : 
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0<=nx<n and 0<=ny<n : 
                            tree[nx][ny].appendleft(1)
    # 겨울
    for i in range(n) : 
        for j in range(n) : 
            fertilizer[i][j] += feed[i][j]
ans = 0
for i in range(n) : 
    for j in range(n) : 
        ans += len(tree[i][j])
print(ans)

