# 시험 감독

import sys
N = int(input())
students = list(map(int,sys.stdin.readline().rstrip().split(' ')))
B,C = map(int,sys.stdin.readline().rstrip().split(' '))
students = [s-B for s in students if s-B>0] # 총감독관 한명씩 투입
answer = N 
for s in students :
    answer += s // C
    if s % C != 0 : 
        answer += 1
print(answer)