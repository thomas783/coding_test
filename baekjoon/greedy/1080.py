# 행렬

def change(i,j) : 
    if a[i][j] == b[i][j] : 
        return 0
    for y in range(i,i+3) : 
        for x in range(j,j+3) : 
            a[y][x] = 1 - a[y][x]
    return 1

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = []
for _ in range(n) : 
    a.append(list(map(int,input().rstrip())))
b = []
for _ in range(n) : 
    b.append(list(map(int,input().rstrip())))
ans = 0
for i in range(n-2) : 
    for j in range(m-2) : 
        ans += change(i,j)
for i in range(n) : 
    for j in range(m) : 
        if a[i][j] != b[i][j] :
            print(-1)
            sys.exit(0)
print(ans)