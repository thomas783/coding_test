# 국영수

import sys

input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n) : 
    name,a,b,c = map(str,input().split())
    li.append([name,int(a),int(b),int(c)])
li = sorted(li,key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(n) :
    print(li[i][0])