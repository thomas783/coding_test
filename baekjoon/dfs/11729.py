# 하노이 탑 이동 순서

import sys

def dfs(n,a,b,c) : 
    if n == 1 : 
        move.append([a,c])
    else : 
        dfs(n-1,a,c,b)
        move.append([a,c])
        dfs(n-1,b,a,c)
n = int(input())
move = []
dfs(n,1,2,3)
print(len(move))
for i in move :
    a,b = i
    print(str(a)+' '+str(b))