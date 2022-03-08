# 수 이어 쓰기2

import sys
input = sys.stdin.readline
n,k = map(int,input().split())
# k가 몇자리수인지 먼저 확인
li = []
tmp = 0
for i in range(len(str(n))) : 
    tmp += i * int(10**i-10**(i-1))
    li.append(tmp)
n = (n - int(10**(len(str(n))-1))+1) * len(str(n))
if n != 0 : 
    li.append(li[-1]+n)
flag = False
for i in range(len(li)) : 
    if k <= li[i] : 
        k_position = i
        flag = True
        break
if not flag : 
    print(-1)
    sys.exit(0)
k -= li[k_position-1]
num = int(10**(i-1)) + k//i -1
leftover = k % i
if leftover == 0 : 
    print(int(str(num)[-1]))
else : 
    print(int(str(num+1)[leftover-1]))