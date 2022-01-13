# 성곽

import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
table = []
for _ in range(m) : 
    table.append(list(map(int,input().split())))
cnt_table = [[0 for _ in range(n)] for _ in range(m)]
dy = [0,-1,0,1]
dx = [-1,0,1,0]
visited = [[-1 for _ in range(n)] for _ in range(m)]
first = 0
second = 0
for i in range(m) : 
    for j in range(n) : 
        tmp = []
        if visited[i][j] == -1 : 
            deq = deque()
            deq.append([i,j])
            visited[i][j] = first
            tmp.append([i,j])
            while deq : 
                y,x = deq.popleft()
                # 다음에 갈수 있는 칸을 bit mask로 구함
                for d in range(4) : 
                    if (1<<d) & (15 ^ table[y][x]) : 
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0<=ny<m and 0<=nx<n and visited[ny][nx]  == -1 :
                            deq.append([ny,nx])
                            visited[ny][nx] = first
                            tmp.append([ny,nx])
            for y,x in tmp : 
                cnt_table[y][x] = len(tmp)
            second = max(second,len(tmp))
            first += 1
print(first)
print(second)
# visited에 그룹이 몇번인지 저장
# cnt_table에 해당 위치의 그룹이 총 몇개씩 있는지 저장
third = 0
for i in range(m) :
    for j in range(n) : 
        for d in range(4) : 
            # 벽 찾기
            if (1<<d) & table[i][j] : 
                ny = i + dy[d]
                nx = j + dx[d]
                if 0<=ny<m and 0<=nx<n and visited[i][j] != visited[ny][nx] : 
                    third = max(third,cnt_table[i][j] + cnt_table[ny][nx])
print(third)