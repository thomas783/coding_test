# 수 묶기

import sys

input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
minus = []
plus = []
zero = 0
for i in li : 
    if i < 0 : 
        minus.append(i)
    elif i > 0 : 
        plus.append(i)
    else : 
        zero += 1
plus.sort(reverse=True)
minus.sort()
ans = 0
for i in range(0,len(plus)-1,2) : 
    if plus[i] == 1 or plus[i+1] == 1 : 
        ans += plus[i] + plus[i+1]
    else : 
        ans += plus[i] * plus[i+1]
if len(plus) % 2 == 1 : 
    ans += plus[-1]
for i in range(0,len(minus)-1,2) : 
    ans += minus[i] * minus[i+1]
if len(minus) % 2 == 1 : 
    if zero == 0 : 
        ans += minus[-1]
print(ans)