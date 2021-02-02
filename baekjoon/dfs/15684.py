# 사다리 조작 

import sys  
def move() : 
    for i in range(N) : 
        num = i
        for j in range(H) : 
            if maps[num][j] : 
                num += 1
            elif maps[num-1][j] : 
                num -= 1
        if i != num : 
            return 0
    return 1

def dfs(cnt, idx, r) : 
    global answer
    if cnt == r : 
        if move() : 
            answer = cnt
        return
    for i in range(idx,H) : 
        for j in range(N-1) : 
            if maps[j][i] : 
                continue
            if j-1 >= 0 and maps[j-1][i] : 
                continue
            if j+1 < N and maps[j+1][i] : 
                continue
            maps[j][i] = 1
            dfs(cnt+1,i,r)
            maps[j][i] = 0

input = sys.stdin.readline
N,M,H = map(int,input().split())
maps = [[0] * H for _ in range(N)]
for _ in range(M) : 
    x,y = map(int,input().split())
    maps[y-1][x-1] = 1
answer, flag = sys.maxsize, 1
for r in range(4) : 
    dfs(0,0,r)
    if answer != sys.maxsize :
        print(answer)
        flag = 0
        break
if flag : 
    print(-1)