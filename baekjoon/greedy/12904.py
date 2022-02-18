# A와 B

import sys

input = sys.stdin.readline
s = list(map(str,input().rstrip()))
t = list(map(str,input().rstrip()))
for _ in range(len(t)-len(s)) : 
    if t[-1] == 'A' : 
        t = t[:-1]
    else : 
        t = t[:-1][::-1]
if s ==t : 
    print(1)
else : 
    print(0)