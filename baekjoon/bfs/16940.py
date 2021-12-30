# BFS 스페셜 저지

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dic = [[] for _ in range(N+1)]
for i in range(N-1) : 
    i,j = map(int,input().split())
    dic[i].append(j)
    dic[j].append(i)
li = list(map(int,input().split()))
visited = [0 for _ in range(N+1)]
# 초기 상태 세팅
visited[1] = 1
deq = deque()
deq.append(1)
idx = 1
flag = True # 정답 여부
while deq : 
    temp = deq.popleft()
    next_ = []
    temp = dic[temp]
    for t in temp : 
        if visited[t] == 0 : 
            visited[t] = 1
            next_.append(t)
    cnt = len(next_)
    # 다음 bfs 애들과 주어진 리스트가 같은지 확인
    if set(next_) != set(li[idx:idx+cnt]) :
        flag = False
        break
    # 주어진 다음 리스트를 큐에 추가
    deq += li[idx:idx+cnt]
    idx += cnt
if flag : 
    print(1)
else : 
    print(0)