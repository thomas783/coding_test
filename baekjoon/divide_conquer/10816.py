# 숫자 카드

import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
m = int(input())
ms = list(map(int,input().split()))
dic = dict()
for i in li : 
    if i in dic : 
        dic[i] += 1
    else : 
        dic[i] = 1
ans = []
for i in ms : 
    if i in dic : 
        ans.append(str(dic[i]))
    else : 
        ans.append('0')
print(' '.join(ans))