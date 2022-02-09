# 잃어버린 괄호

import sys

input = sys.stdin.readline
strings = input().rstrip()
strings = strings.replace(' ','')
ans = []
tmp = strings.split('-')
for t in tmp :
    plus = t.split('+')
    ans.append(sum([int(i) for i in plus]))
if len(ans) == 1 : 
    print(ans[0])
else : 
    print(ans[0] - sum(ans[1:]))