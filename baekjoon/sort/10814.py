# 나이순 정렬

import sys

input = sys.stdin.readline
n = int(input())
li = [list(map(str,input().split()))+[i] for i in range(n)]
li = [[int(i),j,k] for i,j,k in li]
li = sorted(li,key=lambda x:(x[0],x[2]))
for i,j,k in li : 
    print(str(i)+' '+j)