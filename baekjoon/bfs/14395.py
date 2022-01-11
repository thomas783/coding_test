# 4연산

import sys
from collections import deque

input = sys.stdin.readline
s,t = map(str,input().split())
if s == t : 
    print(0)
    sys.exit(0)
deq = deque()
deq.append([s,''])
visited = [s]
ans = []
# arr는 아스키코드 순으로 저장
arr = ['*','+','-','/']
while deq : 
    num, can = deq.popleft()
    for a in arr : 
        if (a == '/' and num == '0') or int(num) > 10**9 :
            continue
        else : 
            num2 = str(int(eval(num + a + num)))
            if num2 not in visited : 
                if num2 == str(t) :
                    if len(ans) == 0 or len(can+a) <= len(ans[-1]) :  
                        ans.append(can+a)
                    else : 
                        continue
                else : 
                    deq.append([num2,can+a])
                    visited.append(num2)
ans = sorted(ans)
if len(ans) == 0 : 
    print(-1)
else : 
    print(ans[0])