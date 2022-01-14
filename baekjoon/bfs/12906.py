# 새로운 하노이 탑

from collections import deque

visited = set()
deq = deque()
a = input().split()
s1 = a[-1] if len(a)>1 else ''
a = input().split()
s2 = a[-1] if len(a)>1 else ''
a = input().split()
s3 = a[-1] if len(a)>1 else ''
deq.append((s1,s2,s3,0))
while deq : 
    a,b,c,cnt = deq.popleft()
    curr_str = a + '/' + b + '/' + c
    if a == len(a)*'A' and b == len(b) * 'B' and c == len(c) * 'C' : 
        print(cnt)
        break
    if curr_str not in visited : 
        visited.add(curr_str)
        if len(a) > 0 :
            deq.append((a[:-1],b+a[-1],c,cnt+1))
            deq.append((a[:-1],b,c+a[-1],cnt+1))
        if len(b) > 0 : 
            deq.append((a+b[-1],b[:-1],c,cnt+1))
            deq.append((a,b[:-1],c+b[-1],cnt+1))
        if len(c) > 0 : 
            deq.append((a+c[-1],b,c[:-1],cnt+1))
            deq.append((a,b+c[-1],c[:-1],cnt+1))