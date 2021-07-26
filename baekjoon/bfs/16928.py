# 뱀과 사다리 게임

from collections import deque
N,M = list(map(int,input().split()))
ladder = dict()
for _ in range(N) : 
    a,b = map(int,input().split())
    ladder[a] = b
snake = dict()
for _ in range(M) : 
    a,b = map(int,input().split())
    snake[a] = b
q = deque()
visited = [False for _ in range(101)]
start = [1,0]
q.append(start)
visited[1] = True
ans = []
while q : 
    temp,cnt = q.popleft()
    if temp == 100 : 
        ans.append(cnt)
        continue
    for i in range(1,7) : 
        nx = temp + i
        if nx <= 100 : 
            if nx in ladder.keys() : 
                nx = ladder[nx]
            if nx in snake.keys() : 
                nx = snake[nx]
            if not visited[nx] :
                visited[nx] = True
                q.append([nx,cnt+1])
print(min(ans))