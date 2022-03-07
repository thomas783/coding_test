# 카드

import sys

input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
dic = dict()
for i in li : 
    if i in dic : 
        dic[i] += 1
    else : 
        dic[i] = 0
print(sorted(dic.items(),key=lambda x:(-x[1],x[0]))[0][0])