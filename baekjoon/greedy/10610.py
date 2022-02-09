# 30

import sys
s = list(input())
if '0' in s : 
    s.remove('0')
else : 
    print(-1)
    sys.exit(0)
if sum([int(i) for i in s]) % 3 == 0 :
    s.sort(reverse=True)
    print(int(''.join(s)+'0'))
else : 
    print(-1)