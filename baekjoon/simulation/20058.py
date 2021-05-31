import sys
from copy import deepcopy
def rotate(L,table) : 
    val = 2 ** L
    start = [0,0]
    x_start,y_start = 0,0
    x_end,y_end = 2 ** L,2 ** L
    temp_table = [[0 for _ in range(2**L)] for _ in range(2**L)]
    while x_end != len(table) and y_end != len(table) :  
        for x,y,tx,ty in zip(range(x_start,x_end),range(y_start,y_end),range(2**L),range(2**L)) :
            temp_table[tx][ty] = table[x][y]
        temp_table = [list(i)[::-1] for i in zip(*temp_table)]
        for x,y,tx,ty in zip(range(x_start,x_end),range(y_start,y_end),range(2**L),range(2**L)) :
            table[x][y] = temp_table[tx][ty]
        


input = sys.stdin.readline
N,Q = list(map(int,input().split()))
table = []
for _ in range(2**N) : 
    table.append(list(map(int,input().split())))
step = list(map(int,input().split()))
L = step[0]
print(rotate(L,table))