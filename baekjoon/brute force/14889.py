# 스타트와 링크

import sys
import itertools

input = sys.stdin.readline
N = int(input())
table = []
for _ in range(N) : 
    table.append(list(map(int,input().split())))
ans = sys.maxsize
for i in itertools.combinations(list(range(N)),N//2) :
    team1,team2 = 0,0
    can1,can2 = list(i), [j for j in list(range(N)) if j not in i]
    for k in itertools.combinations(can1,2) : 
        n1,n2 = list(k)
        team1 += table[n1][n2] + table[n2][n1]
    for k in itertools.combinations(can2,2) : 
        n1,n2 = list(k)
        team2 += table[n1][n2] + table[n2][n1]
    temp_ans = abs(team1-team2)
    ans = min(ans,temp_ans)
    if ans == 0 : 
        break
print(ans)
