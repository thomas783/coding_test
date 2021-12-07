# 연산자 끼워넣기 (2)

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
min = 1000000000
max = -1000000000
N = int(input())
li = list(map(int,input().split()))
cal = list(map(int,input().split()))
deq = deque()
deq.append([li[0],cal,0])
sign = ['+','-','*','//']
while deq : 
    num,cals,curr = deq.popleft()
    if curr == N - 1 :
        if num < min : 
            min = num
        if num > max : 
            max = num
    else : 
        for i in range(4) : 
            if cals[i] != 0 :
                if i == 3 and num < 0 :
                    temp = -int(eval(str(-num) + sign[i] + str(li[curr+1])))
                else :
                    temp = int(eval(str(num) + sign[i] + str(li[curr+1])))
                cals[i] -= 1
                cals_copy = deepcopy(cals)
                deq.append([temp,cals_copy,curr+1])
                cals[i] += 1
print(max,min)

