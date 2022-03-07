# 좌표 정렬하기 2

import sys

n = int(input())
li = []
for _ in range(n) : 
    li.append(list(map(int,input().split())))
li = sorted(li,key=lambda x:(x[1],x[0]))
for i,j in li : 
    print(str(i)+' '+str(j))