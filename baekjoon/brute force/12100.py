# 2048(Easy)

import sys
from copy import deepcopy
def tilt(d,table) :
    table = deepcopy(table)
    global ans
    check = [[0 for _ in range(N)] for _ in range(N)]
    # 0인 경우 아래로 기울이기
    if d == 1 : # 위로 기울이기
        table = table[::-1]
    if d == 2 : # 왼쪽으로 기울이기
        table = [list(i) for i in zip(*table)][::-1]
    if d == 3 : # 오른쪽으로 기울이기
        table = [list(i) for i in zip(*table[::-1])]
    for x in range(N) : 
        for y in range(N-1,-1,-1) : 
            while True : 
                if table[y][x] != 0 : 
                    # 합쳐지는 경우
                    if 0<=y+1<N and table[y+1][x] == table[y][x] and check[y][x] == 0 and check[y+1][x] == 0 : 
                        table[y+1][x],table[y][x] = table[y+1][x]*2, 0
                        check[y+1][x] = 1
                        ans = max(ans,table[y+1][x])
                        y += 1
                    # 아래가 비어있는 경우
                    elif 0<=y+1<N and table[y+1][x] == 0 : 
                        table[y+1][x],table[y][x] = table[y][x],0
                        check[y+1][x],check[y][x] = check[y][x],0
                        y += 1
                    else : 
                        break
                else : 
                    break
    if d == 1 : 
        table = table[::-1]
    if d == 2 : 
        table = [list(i) for i in zip(*table[::-1])]
    if d == 3 :
        table = [list(i) for i in zip(*table)][::-1]
    return table

def dfs(table,n) : 
    if n == 5 : 
        return
    for d in range(4) : 
        new_table = tilt(d,table)
        dfs(new_table,n+1)

ans = 0
input = sys.stdin.readline
N = int(input())
table = []
for y in range(N) :
    table.append(list(map(int,input().split())))
for y in range(N) : 
    for x in range(N) :
        ans = max(table[y][x],ans)
if __name__ == '__main__' : 
    dfs(table,0)
    print(ans)