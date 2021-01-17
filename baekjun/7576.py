# 토마토

import sys
from collections import deque
def check_ripe(farm,M,N,deq,num) : # bfs 사용
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while deq : 
        i,j,ans = deq.popleft()
        for idx in range(4) : 
            next_i = i + dx[idx]
            next_j = j + dy[idx]
            if 0<=next_i<N and 0<=next_j<M and farm[next_i][next_j] == 0 : 
                farm[next_i][next_j] = 1
                deq.append([next_i,next_j,ans+1])
                num -= 1
    return [num,ans]

M, N = map(int,sys.stdin.readline().rstrip().split(' '))
farm = []
for _ in range(N) : 
    farm.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
deq = deque()
num = 0
for i in range(N) : 
    for j in range(M) : 
        if farm[i][j] == 1 : 
            deq.append([i,j,0])
        if farm[i][j] == 0 : # 총 없애야하는 안익은 토마토 개수 세기
            num += 1
num,answer = check_ripe(farm,M,N,deq,num)
if num == 0 :
    print(answer)
else : 
    print(-1)