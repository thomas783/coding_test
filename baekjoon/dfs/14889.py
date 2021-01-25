# 스타트와 링크
# pypy3으로 밖에 못품...
    
import sys
from itertools import combinations

def dfs(idx,cnt) : 
    global answer
    if cnt == N // 2 :
        team1,team2 = 0,0
        for i in range(N) : 
            for j in range(N) : 
                if select[i] and select[j] : 
                    team1 += power[i][j]
                elif not select[i] and not select[j] : 
                    team2 += power[i][j]
        answer = min(answer,abs(team1-team2))
    for i in range(idx,N) :
        if select[i] : 
            continue
        select[i] = 1
        dfs(i+1,cnt+1)
        select[i] = 0

N = int(input())
power = []
for _ in range(N) : 
    power.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
select = [0 for _ in range(N)]
answer = sys.maxsize
dfs(0,0)
print(answer)