# 전구와 스위치

import sys
from copy import deepcopy

# 첫번째 전구를 켜는 경우와 그렇지 않은 경우를 두가지로 나누어서 계산해본다
input = sys.stdin.readline
n = int(input())
curr = list(map(int,input().rstrip()))
target = list(map(int,input().rstrip()))
ans1, ans2 = 0,1
if n > 2 :
    curr_2 = [1-k for k in curr[0:2]] + curr[2:]
elif n == 2 : 
    curr_2 = [1-k for k in curr[0:2]]
for i in range(1,n-1) : 
    if curr[i-1] != target[i-1] :
        curr[i-1:i+2] = [1-k for k in curr[i-1:i+2]]
        ans1 += 1
    if curr_2[i-1] != target[i-1] :
        curr_2[i-1:i+2] = [1-k for k in curr_2[i-1:i+2]]
        ans2 += 1
if curr[n-2] != target[n-2] : 
    curr[n-2:] = [1-k for k in curr[n-2:]]
    ans1 += 1
if curr_2[n-2] != target[n-2] : 
    curr_2[n-2:] = [1-k for k in curr_2[n-2:]]
    ans2 += 1
if curr != target : 
    ans1 = sys.maxsize
if curr_2 != target : 
    ans2 = sys.maxsize
final_ans = min(ans1,ans2)
if final_ans == sys.maxsize : 
    print(-1)
else : 
    print(final_ans)