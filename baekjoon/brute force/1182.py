# 부분수열의 합

from itertools import combinations
import sys
input = sys.stdin.readline
N,S = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0
for i in range(1,len(li)+1) : 
    for c in combinations(li,i) : 
        if sum(c) == S : 
            cnt += 1
print(cnt)