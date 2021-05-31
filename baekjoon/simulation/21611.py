import sys
from collections import deque

input = sys.stdin.readline
N,M = list(map(int,input().split()))
table = []
for _ in range(N) : 
    table.append(list(map(int,input().split())))
magic = []
for _ in range(M) : 
    x,y = list(map(int,input().split()))
    magic.append([x-1,y])
dic = {1:0,2:0,3:0}
li = []
start = [N//2,N//2]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(1,N) : 
    if i % 2 == 1 :
        li += [2] * i
        li += [1] * i
    else : 
        li += [3] * i
        li += [0] * i
li += [2] * (N-1)
for d,s in magic :
    # 블리자드 마법 시전
    x,y = start
    for i in range(1,s+1) : 
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        table[nx][ny] = -1
    # 구슬 이동
    q = deque()
    for dir in li : 
        nx = x + dx[dir]
        ny = y + dy[dir]
        if table[nx][ny] != -1 : 
            q.append(table[nx][ny])
        x,y = nx,ny
    # 구슬 폭발
    while True :
        flag = len(q)
        next_q = deque()
        temp_q = deque()
        while q : 
            temp = q.popleft()
            if q == 0 :
                continue
            if not temp_q : 
                temp_q.append(temp)
            else :
                if temp != temp_q[-1] : 
                    if len(temp_q) >= 4 : 
                        dic[temp_q[-1]] += len(temp_q)
                        temp_q = deque()
                        temp_q.append(temp)
                    else : 
                        next_q += temp_q
                        temp_q = deque()
                        temp_q.append(temp)
                else : 
                    temp_q.append(temp)
        if 0< len(temp_q) < 4 : 
            next_q += temp_q
        if flag == len(next_q) : 
            break
        else : 
            q = next_q
    # 구슬 변화
    last_q = deque()
    temp_q = deque()
    while next_q : 
        temp = next_q.popleft()
        if not temp_q : 
            temp_q.append(temp)
        else : 
            if temp_q[-1] == temp : 
                temp_q.append(temp)
            else : 
                last_q.append(len(temp_q))
                last_q.append(temp_q[-1])
                temp_q = deque()
                temp_q.append(temp)
    if temp_q : 
        last_q += [len(temp_q),temp_q[-1]]
    last_q += [0] * (N**2 - len(last_q))
    # 원래의 table로 돌리기
    table = [[0 for _ in range(N)] for _ in range(N)]
    x,y = start
    idx = 0
    for dir in li : 
        nx = x + dx[dir]
        ny = y + dy[dir]
        table[nx][ny] = last_q[idx]
        x,y = nx,ny
        idx += 1
answer = 0
for i in range(1,4) : 
    answer += dic[i] * i
print(answer)