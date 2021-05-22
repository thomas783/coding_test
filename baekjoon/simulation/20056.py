import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
N,M,K = map(int,input().split())
q = deque()
table = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M) : 
    x,y,m,s,d = map(int,input().split())
    table[x-1][y-1].append([m,s,d])
    q.append([x-1,y-1])
for _ in range(K) : 
    temp = []
    for _ in range(len(q)) : 
        x,y = q.popleft()
        for _ in range(len(table[x][y])) : 
            m,s,d = table[x][y].popleft()
            nx = (s * dx[d] + x) % N
            ny = (s * dy[d] + y) % N
            q.append([nx,ny])
            temp.append([nx,ny,m,s,d])
    for x,y,m,s,d in temp : 
        table[x][y].append([m,s,d])
    for i in range(N) : 
        for j in range(N) : 
            if len(table[i][j]) > 1 : 
                nm, ns, odd, even, flag = 0,0,0,0,0
                for idx, [m,s,d] in enumerate(table[i][j]) :
                    nm += m
                    ns += s
                    if idx == 0 : 
                        if d % 2 == 0 : 
                            even = 1
                        else : 
                            odd = 1
                    else : 
                        if even == 1 and d % 2 == 1 : 
                            flag = 1
                        elif odd == 1 and d % 2 == 0 :
                            flag = 1
                nm //= 5
                ns //= len(table[i][j])
                table[i][j] = deque()
                if nm != 0 : 
                    for idx in range(4) : 
                        nd = 2 * idx if flag == 0 else 2 * idx + 1
                        table[i][j].append([nm,ns,nd])
answer = 0
for i in range(N) : 
    for j in range(N) :
        if table[i][j] :
            for m,s,d in table[i][j] : 
                answer += m
print(answer)