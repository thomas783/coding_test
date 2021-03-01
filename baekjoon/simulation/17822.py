# 원판 돌리기

import sys
import copy
from collections import deque
def change(circle,x,d,k) : # 회전시키는 함수
    for i in range(1,N+1) : 
        if i % x == 0 : 
            if d == 0 : 
                for _ in range(k) : 
                    circle[i] = [circle[i][-1]] + circle[i][:-1]
            else : 
                for _ in range(k) : 
                    circle[i] = circle[i][1:] + [circle[i][0]]

def check(circle) : # 인접한 수 제거하는 함수
    temp = copy.deepcopy(circle)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(1,N+1) : 
        for j in range(M) : 
            if temp[i][j] != 0 : 
                deq = deque() # bfs
                deq.append([i,j])
                visited = [[i,j]]
                start = temp[i][j]
                while deq : 
                    x,y = deq.popleft()
                    for k in range(4) : 
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if ny == -1 : ny = M -1
                        elif ny == M : ny = 0
                        if 0<nx<=N and 0<=ny<M and start == temp[nx][ny] and [nx,ny] not in visited :
                            deq.append([nx,ny])
                            visited.append([nx,ny])
                if len(visited) >1 : 
                    for x,y in visited : 
                        temp[x][y] = 0
    return temp


input = sys.stdin.readline
N,M,T = map(int,input().split())
circle = [[]]
for _ in range(N) : 
    circle.append(list(map(int,input().split())))
moves = []
for _ in range(T) : 
    moves.append(list(map(int,input().split())))
for x,d,k in moves : 
    change(circle,x,d,k)
    if circle != check(circle) : 
        circle = check(circle)
    else : # 인접해서 지울수 있는 것이 없는 경우
        aveg = 0
        cnt = 0
        for i in range(1,N+1) :
            for j in range(M) : 
                if circle[i][j] != 0 :  
                    aveg += circle[i][j]
                    cnt += 1
        if cnt == 0 : 
            break
        aveg = aveg / cnt
        for i in range(1,N+1) : 
            for j in range(M) : 
                if circle[i][j] != 0 : 
                    if circle[i][j] > aveg : 
                        circle[i][j] -= 1
                    elif circle[i][j] < aveg : 
                        circle[i][j] += 1
answer = 0
for i in range(1,N+1) : 
    for j in range(M) : 
        if circle[i][j] != 0 : 
            answer += circle[i][j]
print(answer)