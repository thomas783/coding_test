# 돌 그룹

import sys
from collections import deque
def bfs(rock) : 
    rock = sorted(rock)
    deq = deque()
    deq.append(rock)
    visited = [[0 for _ in range(2001)] for _ in range(2001)]
    visited[rock[0]][rock[2]] = rock[1]
    while deq : 
        a,b,c = deq.popleft()
        # 모두 같은 경우
        if a == b and b == c : 
            return 1
        # 모두 다른 경우
        elif a !=b and b != c and c != a : 
            can = [sorted([2*a,b,c-a]),sorted([2*a,b-a,c]),sorted([a,b*2,c-b])]
            for c in can : 
                if visited[c[0]][c[2]] == 0 : 
                    deq.append(c)
                    visited[c[0]][c[2]] = c[1]
        # 두개만 같은 경우
        else : 
            can = sorted([2*a,b,c-a])
            if visited[can[0]][can[2]] == 0 : 
                deq.append(can)
                visited[can[0]][can[2]] = can[1]
    return 0
input = sys.stdin.readline
rock = list(map(int,input().split()))
if __name__ == '__main__' : 
    print(bfs(rock))