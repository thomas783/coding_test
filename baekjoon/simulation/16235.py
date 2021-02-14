# 나무 재테크

import sys
from collections import deque
N,M,K = map(int,sys.stdin.readline().rstrip().split(' '))
food = []
for _ in range(N) : 
    food.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
area = [[5 for j in range(N)] for i in range(N)]
tree = [[deque() for j in range(N)] for i in range(N)]
for _ in range(M) : 
    x,y,z = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    tree[x-1][y-1].append(z)
dead = []
for _ in range(K) : 
    # 봄
    for i in range(N) : 
        for j in range(N) : 
            t_len = len(tree[i][j])
            for k in range(t_len) : 
                if area[i][j] >= tree[i][j][k] : 
                    area[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else : 
                    for _ in range(k,t_len) : # 여름
                        area[i][j] += tree[i][j].pop()//2
                    break
    # 가을
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for x in range(N) : 
        for y in range(N) : 
            for t in tree[x][y] : 
                if t % 5 == 0 : 
                    for i in range(8) : 
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<N and 0<=ny<N :
                            tree[nx][ny].appendleft(1)
    # 겨울
    for i in range(N) : 
        for j in range(N) : 
            area[i][j] += food[i][j]
answer = 0
for i in range(N) : 
    for j in range(N) : 
        answer += len(tree[i][j])
print(answer)