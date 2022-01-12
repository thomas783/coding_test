# 탈옥

import sys
from collections import deque

# 현재 상황에 죄수 둘다 탈출 가능한가
def bfs(y,x) : 
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    deq = deque()
    deq.append([y,x])
    visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]
    visited[y][x] = 0
    while deq : 
        y,x = deq.popleft()
        for d in range(4) :
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<h+2 and 0<=nx<w+2 :
                if visited[ny][nx] == -1 : 
                    if table[ny][nx] == '.' or table[ny][nx] == '$' : 
                        visited[ny][nx] = visited[y][x]
                        # 최대한 짧게 갈수 있도록 appendleft해줌
                        deq.appendleft([ny,nx])
                    elif table[ny][nx] == '#' : 
                        visited[ny][nx] = visited[y][x] + 1
                        deq.append([ny,nx])
    return visited

input = sys.stdin.readline
n = int(input())
for _ in range(n) : 
    h,w = map(int,input().split())
    table = [['.' for _ in range(w+2)]]
    for _ in range(h) : 
        table.append(list('.'+input().rstrip()+'.'))
    table.append(['.' for _ in range(w+2)])
    prisoner = []
    for i in range(h+2) : 
        for j in range(w+2) : 
            if table[i][j] == '$' : 
                prisoner.append([i,j])
    # 죄수부터 나오는 경우
    first = bfs(prisoner[0][0],prisoner[0][1])
    second = bfs(prisoner[1][0],prisoner[1][1])
    # 상근이가 구해주는 경우
    third = bfs(0,0)
    ans = sys.maxsize
    for i in range(h+2) : 
        for j in range(w+2) : 
            if first[i][j] != -1 and second[i][j] != -1 and third[i][j] != -1 : 
                # 해당 위치까지 벽을 열어야하는 총 합
                ans_tmp = first[i][j] + second[i][j] + third[i][j]
                # 해당 위치가 벽이라면 한명만 열어도 됨
                if table[i][j] == '#' : 
                    ans_tmp -= 2
                ans = min(ans,ans_tmp)
    print(ans)