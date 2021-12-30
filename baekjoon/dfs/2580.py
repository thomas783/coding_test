# 스도쿠

import sys
def dfs(n,N,zeros,table) :
    if n == 0 : 
        for t in table : 
            print(' '.join(list(map(str,t))))
        sys.exit(0)
    cur = zeros[N-n]
    li = list(range(1,10))
    for k in range(9) : 
        if table[cur[0]][k] in li : # 같은 행 확인
            li.remove(table[cur[0]][k])
        if table[k][cur[1]] in li : # 같은 열 확인
            li.remove(table[k][cur[1]])
    for y in range(cur[0]//3*3,cur[0]//3*3+3) : # 같은 네모 확인
        for x in range(cur[1]//3*3,cur[1]//3*3+3) : 
            if table[y][x] in li : 
                li.remove(table[y][x])
    for val in li : 
        table[cur[0]][cur[1]] = val
        dfs(n-1,N,zeros,table)
        table[cur[0]][cur[1]] = 0

input = sys.stdin.readline
table = []
zeros = []
for y in range(9) : 
    x = list(map(int,input().split()))
    table.append(x)
    for k in range(9) : 
        if x[k] == 0 : 
            zeros.append([y,k])
n = len(zeros)
dfs(n,n,zeros,table)