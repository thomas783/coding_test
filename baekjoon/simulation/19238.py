# 스타트 택시
# 안풀려서 인터넷 참고함 
# import sys
# from collections import deque
# def bfs(start,finish,area) : 
#     if start == finish : 
#         return 0
#     visited = [start]
#     deq = deque()
#     deq.append(start+[0])
#     while deq : 
#         x,y,val = deq.popleft()
#         dx = [0,0,1,-1]
#         dy = [1,-1,0,0]
#         for i in range(4) : 
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if [nx,ny] == finish : 
#                 return val+1
#             else : 
#                 if 0<=nx<N and 0<=ny<N and [nx,ny] not in visited and area[nx][ny] != 1 : 
#                     visited.append([nx,ny])
#                     deq.append([nx,ny,val+1])
#     return -1

# input = sys.stdin.readline
# N,M,fuel = list(map(int,input().split()))
# area = []
# for _ in range(N) : 
#     area.append(list(map(int,input().split())))
# taxi = [i-1 for i in map(int,input().split())]
# customer = []
# for _ in range(M) : 
#     temp = [i-1 for i in map(int,input().split())]
#     customer.append([temp[:2],temp[2:]])
# answer = 0
# check = [True for _ in range(M)]
# while True in check : 
#     mini = sys.maxsize
#     temp = []
#     for i in range(len(customer)) : 
#         if check[i] : 
#             val = bfs(taxi,customer[i][0],area)
#             if -1<val<mini : 
#                 temp = [customer[i][0][0],customer[i][0][1],val,i]
#                 mini = val
#             elif val == mini : 
#                 if temp[0]>customer[i][0][0] : 
#                     temp = [customer[i][0][0],customer[i][0][1],val,i]
#                 elif temp[0] == customer[i][0][0] :
#                     if temp[1] > customer[i][0][1] : 
#                         temp = [customer[i][0][0],customer[i][0][1],val,i]
#     if not temp : 
#         answer = -1
#         break
#     taxi = temp[:2] # 승객 위치로 이동
#     fuel -= temp[2]
#     fuel -= bfs(taxi,customer[temp[3]][1],area)
#     if fuel < 0 : 
#         answer = - 1
#         break
#     else : 
#         fuel += bfs(taxi,customer[temp[3]][1],area) * 2
#         taxi = customer[temp[3]][1]
#         check[temp[3]] = False
# if answer != -1 : 
#     answer = fuel
# print(answer)


import sys
from collections import deque
from heapq import heappop, heappush

n, m, f = map(int, sys.stdin.readline().rstrip().split())
arr = [[] for i in range(n)]
INF = int(1e9)
d = [[1,0], [-1,0], [0,1], [0,-1]]

for i in range(n):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = x


taxi_pos = list(map(int, sys.stdin.readline().rstrip().split()))
srcs = [[] for i in range(m)]
dsts = [[] for i in range(m)]

for i in range(m):
    src_y, src_x, dst_y, dst_x = map(int, sys.stdin.readline().rstrip().split())
    srcs[i] = [src_y, src_x]
    dsts[i] = [dst_y, dst_x]

picked = [False for _ in range(m)]

def isin(y,x):
    if -1<y<n:
        if -1<x<n: return True
    return False

# 출발지와 도착지 거리 계산
def bfs():
    global taxi_pos, f
    sy, sx = taxi_pos[0] - 1, taxi_pos[1] - 1
    check = [[False for _ in range(n)] for _ in range(n)]
    table = [[INF for _ in range(n)] for _ in range(n)]
    q = deque([])
    table[sy][sx] = 0
    q.append([sy, sx])
    check[sy][sx] = True
    
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if isin(ny, nx):
                if not check[ny][nx]:
                    check[ny][nx] = True
                    if arr[ny][nx] != 1:
                        table[ny][nx] = table[y][x] + 1
                        q.append([ny, nx])
    
    return table

# 택시와 가까운 손님을 찾는 함수
def find_guest():
    global arr, f, picked 
    table = bfs()
    pq = []

    for i in range(m):
        if not picked[i]:
            y, x = srcs[i][0] - 1, srcs[i][1] - 1
            dist = table[y][x]
            if f - dist >= 0:
                heappush(pq, [dist, y, x, i]) 

    if not pq: return -1
    dist, _, _, guest_index = heappop(pq)
    f -= dist
    picked[guest_index] = True

    return guest_index

# 손님의 목적지까지 가는 함수
def go_dst(guest_index):
    global f
    table = bfs()
    y, x = dsts[guest_index][0] - 1, dsts[guest_index][1] - 1
    dist = table[y][x]
    if f - dist < 0: return -1
    return dist

# 실행코드
ok = True
cnt = m
while cnt:
    guest_index = find_guest()
    if guest_index == -1:
        ok = False
        break
    taxi_pos = srcs[guest_index]
    dist = go_dst(guest_index)
    if dist == -1:
        ok = False
        break
    f += dist
    taxi_pos = dsts[guest_index]
    cnt -= 1

if ok: print(f)
else: print(-1)