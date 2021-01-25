# 연산자 끼워넣기

import sys
from collections import deque
N = int(input())
num = list(map(int,sys.stdin.readline().rstrip().split(' ')))
operator = list(map(int,sys.stdin.readline().rstrip().split(' ')))
deq = deque()
cnt = 0
deq.append([num[0],operator,cnt])
answer = []
while deq : 
    temp = deq.popleft()
    temp_answer = temp[0]
    temp_operator = temp[1]
    temp_cnt = temp[2]
    if temp_cnt == N-1 : 
        answer.append(temp_answer)
    else : 
        if temp_operator[0] != 0 : # 덧셈
            deq.append([temp_answer + num[temp_cnt+1],[temp_operator[0]-1] + temp_operator[1:],temp_cnt+1])
        if temp_operator[1] != 0 : # 뺼셈 
            deq.append([temp_answer - num[temp_cnt+1],[temp_operator[0]] + [temp_operator[1]-1] + temp_operator[2:],temp_cnt+1])
        if temp_operator[2] != 0 : # 곱셈
            deq.append([temp_answer * num[temp_cnt+1],temp_operator[0:2] + [temp_operator[2]-1] + [temp_operator[3]],temp_cnt+1])
        if temp_operator[3] != 0 : # 나눗셈
            if temp_answer >0 : 
                deq.append([temp_answer // num[temp_cnt+1],temp_operator[0:3] + [temp_operator[3]-1],temp_cnt+1])
            else : 
                deq.append([-(-temp_answer // num[temp_cnt+1]),temp_operator[0:3] + [temp_operator[3]-1],temp_cnt+1])
print(max(answer))
print(min(answer))