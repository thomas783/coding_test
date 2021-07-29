# 가르침
# pypy3으로 뚫림

from itertools import combinations
N, K = map(int,input().split())
li = []
for _ in range(N) : 
    li.append(input()[4:-4])
alpha = ['a','n','t','i','c']
can = ['b','d','e','f','g','h','j','k','l','m',
    'o','p','q','r','s','u','v','w','x','y','z']
ans = 0
if K < 5 : 
    print(ans)
else : 
    for i in combinations(can,K-5) : 
        temp = alpha + [j for j in i]
        temp_ans = 0
        for a in li : 
            flag = True
            for b in a : 
                if b not in temp : 
                    flag = False
                    break
            if flag : 
                temp_ans += 1
        ans = max(ans,temp_ans)
    print(ans)
