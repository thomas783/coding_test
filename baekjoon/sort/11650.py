# 좌표 정렬하기

import sys
from collections import defaultdict

dic = defaultdict()
for i in range(-100000,100001) : 
    dic[i] = []
n = int(input())
for _ in range(n) : 
    i,j = map(int,input().split())
    dic[i].append(j)
ans = []
for i in range(-100000,100001) :
    tmp = sorted(dic[i])
    for j in tmp : 
        ans.append([i,j])
for x,y in ans : 
    print(str(x)+' '+str(y))