# 회의실 배정

import sys
input = sys.stdin.readline
n = int(input())
conf = []
for _ in range(n) : 
    conf.append(list(map(int,input().split())))
conf = sorted(conf,key=lambda x : (x[1],x[0]))
ans = 0
curr_time = 0
for i in range(n) :
    if conf[i][0] >= curr_time : 
        ans += 1
        curr_time = conf[i][1]
print(conf)
print(ans)