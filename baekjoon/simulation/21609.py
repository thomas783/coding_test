import sys
from collections import deque

def find_block(table) : 
    global N
    global answer
    global flag
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    block = []
    visited = []
    br = []
    q = deque()
    for x in range(N) : 
        for y in range(N) : 
            if table[x][y] != [] and table[x][y] != 0 and table[x][y] != -1 : 
                q.append([x,y])
            else : 
                br.append([x,y])
    while q : 
        x,y = q.popleft() 
        color = [table[x][y],0]
        rainbow = 0
        temp_block = deque()
        temp_q = deque()
        if [x,y] not in br and [x,y] not in visited : 
            temp_block.append([x,y])
            temp_q.append([x,y])
            while temp_q : 
                temp_x,temp_y = temp_q.popleft()
                for d in range(4) : 
                    nx = temp_x + dx[d]
                    ny = temp_y + dy[d]
                    if 0<=nx<N and 0<=ny<N and table[nx][ny] in color and [nx,ny] not in temp_block:
                        temp_block.append([nx,ny])
                        temp_q.append([nx,ny])
                        if table[nx][ny] == 0 : 
                            rainbow += 1
            for i,j in temp_block :
                if table[i][j] != 0 : 
                    visited.append([i,j])
            temp_block.append(rainbow)
            block.append(temp_block)
    block = [list(i) for i in block]
    final_block = []
    for b in block : 
        final_block.append(sorted(b[:-1]) + [b[-1]] + [sorted([[x,y] for x,y in b[:-1] if table[x][y] != 0])[0]])
    if final_block : 
        final_block = sorted(final_block, key = lambda x : (-len(x),-x[-2],-x[-1][0],-x[-1][1]))
        final_block = final_block[0][:-2]
    if len(final_block) < 2 : 
        flag = False
        return
    answer += len(final_block) ** 2
    for x,y in final_block : 
        table[x][y] = []

def gravity(table) : 
    for i in range(N-1,-1,-1) : 
        for j in range(N-1,-1,-1) : 
            x,y = i,j
            while True :
                if 0<=x+1<N and table[x+1][y] == [] and table[x][y] != -1 :
                    table[x][y],table[x+1][y] = [],table[x][y]
                    x = x+1
                else : 
                    break

answer = 0
input = sys.stdin.readline
N,M = list(map(int,input().split()))
table = []
for _ in range(N) : 
    table.append(list(map(int,input().split())))
flag = True
while flag : 
    find_block(table)
    gravity(table)
    # 90도 회전
    table = [list(t) for t in zip(*table)][::-1]
    gravity(table)
print(answer)