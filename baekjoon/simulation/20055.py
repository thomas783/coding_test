import sys
from collections import deque
input = sys.stdin.readline
N,K = list(map(int,input().split()))
durability = deque(list(map(int,input().split())))
ans = 1
robot = deque([0]*(N*2))
while True : 
    # 1단계
    durability.rotate(1)
    robot.rotate(1)
    robot[N-1] = 0
    # 2단계
    for i in range(N-2,-1,-1) : 
        if robot[i]!=0 and robot[i+1]==0 and durability[i+1]>=1 : 
            durability[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[N-1] = 0
    # 3단계
    if robot[0]==0 and durability[0] > 0 : 
        durability[0] -= 1
        robot[0] = 1
    # 4단계
    cnt = 0
    for i in range(len(durability)) : 
        if durability[i] == 0 : 
            cnt += 1
    if cnt >= K : 
        print(ans)
        break
    ans += 1