# 대회 or 인턴

import sys
n,m,k = map(int,input().split())
team = 0
while True : 
    if n-2 >= 0 and m-1 >= 0 : 
        team += 1
        n -= 2; m -= 1
    else : 
        break
leftover = n+m
k -= leftover 
while k> 0 : 
    k -= 3
    team -= 1
print(team)