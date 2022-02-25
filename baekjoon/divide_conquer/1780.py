# 종이의 개수

import sys

def check(x,y,n) : 
    tmp = table[x][y]
    for i in range(n) :
        for j in range(n) : 
            if tmp != table[x+i][y+j] :
                return False
    return True

def divide(x,y,n) : 
    if check(x,y,n) : 
        ans[table[x][y]+1] += 1
    else : 
        for i in range(3) :
            for j in range(3) : 
                divide(x+i*n//3,y+j*n//3,n//3)
    return
input = sys.stdin.readline
n = int(input())
table = []
for _ in range(n) : 
    table.append(list(map(int,input().split())))
ans = [0,0,0]
divide(0,0,n)
for i in ans :
    print(i)