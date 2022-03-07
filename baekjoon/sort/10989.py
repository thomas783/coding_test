# 수 정렬하기 3

import sys

input = sys.stdin.readline
n = int(input())
dic = dict()
for i in range(1,10001) : 
    dic[i] = 0
for _ in range(n) : 
    dic[int(input())] += 1
for idx,num in dic.items() : 
    for _ in range(num) : 
        print(idx)