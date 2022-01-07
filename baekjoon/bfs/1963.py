# 소수 경로

import sys
import math
from collections import deque
from copy import deepcopy
def is_prime(n) : 
    for i in range(2,int(math.sqrt(n))+1) :
        if n % i == 0 : 
            return False
    return True
input = sys.stdin.readline
T = int(input())
prime = []
for i in range(1001,10000,2) : 
    if is_prime(i) : 
        prime.append(i)
for _ in range(T) : 
    ans = 0
    start, end = map(int,input().split())
    deq = deque()
    deq.append(start)
    visited = [sys.maxsize for _ in range(10000)]
    visited[start] = 0
    can = list(map(str,range(10)))
    while deq : 
        num = str(deq.popleft())
        for i in range(4) : 
            can.remove(num[i])
            for c in can : 
                curr = deepcopy(list(num))
                curr[i] = c
                tmp = int(''.join(curr))
                if tmp >= 1000 and visited[tmp] > visited[int(num)] + 1 and tmp in prime : 
                    visited[tmp] = visited[int(num)] + 1
                    deq.append(tmp)
            can.append(num[i])
        if int(num) == start : 
            visited[int(num)] = sys.maxsize
    if visited[end] == sys.maxsize : 
        print(0)
    else : 
        print(visited[end])