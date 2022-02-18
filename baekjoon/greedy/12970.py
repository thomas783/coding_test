# AB

import sys
n,k = map(int,input().split())
li = ['B' for _ in range(n)]
cnt = 0
for i in range(n) : 
    for j in range(n-1,cnt-1,-1) : 
        li[j] = 'A'
        tmp_cnt = n-j-1
        if cnt*(n-cnt-1) + tmp_cnt == k : 
            print(''.join(li))
            sys.exit(0)
        li[j] = 'B'
    li[cnt] = 'A'
    cnt += 1
print(-1)