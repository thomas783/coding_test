# 부동호
# k의 범위는 2~9, 가능한 k+1자리의 수의 경우는 최대 10!
# 그렇기 때문에 brute force 가능

import sys
from itertools import permutations
li = list(range(10))
k = int(input())
wedge = list(map(str,input().split()))
can = []
for c in permutations(li,k+1) : 
    flag = True
    for i in range(k) : 
        if wedge[i] == '<' and c[i] > c[i+1] : 
            flag = False
            break
        elif wedge[i] == '>' and c[i] < c[i+1] : 
            flag = False
            break
    if flag : 
        can.append(''.join([str(k) for k in c]))
print(can[-1])
print(can[0])