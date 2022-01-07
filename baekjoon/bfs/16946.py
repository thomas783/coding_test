# 벽 부수고 이동하기 4

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
table = []
for _ in range(n) : 
    table.append([int(i) for i in input()[:-1]])
# 벽에 해당하는 것들을 헷갈리니까 -1로 만듬
for i in range(n) : 
    for j in range(m) : 
        if table[i][j] == 1 : 
            table[i][j] = -1
# 이미 갔던 곳을 확인하기 위한 메트릭스
visited = [[False for _ in range(m)] for _ in range(n)]
dic = dict()
dy = [0,0,1,-1]
dx = [1,-1,0,0]
idx = 1
# 벽이 없는 0끼리 몇개씩인지 세서 idx를 붙여서 담아두고 
# 해당 idx에 개수를 담아둠
for i in range(n) : 
    for j in range(m) : 
        if table[i][j] == -1 : 
            visited[i][j] = True
        elif table[i][j] == 0 : 
            cnt = 1
            start = [i,j]
            visited[i][j] = True
            table[i][j] = idx
            deq = deque()
            deq.append(start)
            while deq : 
                y,x = deq.popleft()
                for d in range(4) :
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and table[ny][nx] == 0 : 
                        deq.append([ny,nx])
                        cnt += 1
                        visited[ny][nx] = True
                        table[ny][nx] = idx
            dic[idx] = cnt
            idx += 1
ans = [[0 for _ in range(m)] for _ in range(n)]
for y in range(n) : 
    for x in range(m) : 
        if table[y][x] == -1 : 
            s = 1
            # 중복되는 idx를 피하기 위해 set를 사용
            tmp = set()
            for d in range(4) : 
                ny = y + dy[d]
                nx = x + dx[d]
                if 0<=ny<n and 0<=nx<m and table[ny][nx] != -1 :
                    tmp.add(table[ny][nx])
            for t in tmp : 
                s += dic[t]
            ans[y][x] = s % 10
for a in ans : 
    print(''.join(list(map(str,a))))