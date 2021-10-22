# 구슬 탈출 2

import sys
from copy import deepcopy

def tilt(table,idx) : 
    fin = [False,False] # red,blue 나왔는지 여부
    t = deepcopy(table)
    if idx == 0 : # tilt right
        pass
    elif idx == 1 : # tilt left
        t = [i[::-1] for i in t]
    elif idx == 2 : # tilt up
        t = [list(i) for i in zip(*t[::-1])]
    elif idx == 3 : # tilt down
        t = [list(i) for i in zip(*t)][::-1]
    for j in range(len(t)) : 
        for k in range(len(t[0])-1,-1,-1) : # 가장 오른쪽부터 오른쪽으로 민다
            if t[j][k] == 'B' or t[j][k] == 'R' : 
                while True : 
                    if t[j][k+1] == '.' : 
                        t[j][k], t[j][k+1] = t[j][k+1], t[j][k]
                        k += 1
                    elif t[j][k+1] == 'O' : 
                        if t[j][k] == 'R' : 
                            fin[0] = True
                        elif t[j][k] == 'B' : 
                            fin[1] = True
                        t[j][k] = '.'
                        break
                    elif t[j][k+1] in ['#','R','B'] : 
                        break
    # 원래 형태로 되돌림
    if idx == 1 : 
        t = [i[::-1] for i in t]
    elif idx == 2 : 
        t = [list(i) for i in zip(*t)][::-1]
    elif idx == 3 : 
        t = [list(i) for i in zip(*t[::-1])]
    if fin == [False,False] : # 어느 공도 나오지 못한경우
        return t
    elif fin == [True,False] : # 빨간공만 나온경우
        return True
    else : # 파란공이 나온경우
        return False

def dfs(table) : 
    ans = sys.maxsize
    queue = [[table,0]]
    while queue : 
        tmp,itr = queue.pop(0)
        for i in range(4) : 
            new_table = tilt(tmp,i)
            if new_table == True : 
                ans = min(ans,itr+1)
            elif new_table != tmp and new_table != False and itr + 1 < 10 : 
                queue.append([new_table,itr+1])
    if ans == sys.maxsize : 
        return -1
    else : 
        return ans

input = sys.stdin.readline
N, M = map(int,input().split())
table = []
for _ in range(N) : 
    table.append(list(input())[:-1])
print(dfs(table))