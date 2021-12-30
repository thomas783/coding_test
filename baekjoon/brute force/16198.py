# 에너지 모으기

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
balls = list(map(int,input().split()))
deq = deque()
deq.append([balls,0])
ans = -sys.maxsize
while deq : 
    temp_balls,energy = deq.popleft()
    if len(temp_balls) == 2 : 
        ans = max(ans,energy)
        continue
    for i in range(1,len(temp_balls)-1) : 
        deq.append([temp_balls[:i]+temp_balls[i+1:],energy+temp_balls[i-1]*temp_balls[i+1]])
print(ans)
