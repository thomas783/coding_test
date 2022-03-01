# Z

import sys

def bit_transform(n,r,c) : 
    ans = []
    for i in range(n-1,-1,-1) : 
        ans.append(str(r // 2**i)+str(c // 2**i))
        r = r % 2**i
        c = c % 2**i
    return ans

input = sys.stdin.readline
n,r,c = map(int,input().split())
bit = bit_transform(n,r,c)
dic = {'00':0,'01':1,'10':2,'11':3}
ans = 0
for i in range(n) : 
    ans += dic[bit[i]] * (4**(n-i-1))
print(ans)