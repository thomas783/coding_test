# 롤러코스터

import sys
input = sys.stdin.readline
r,c = map(int,input().split())
table = []
for _ in range(r) : 
    table.append(list(map(int,input().split())))
if r % 2 == 1 : 
    print(('R'*(c-1)+'D'+'L'*(c-1)+'D')*(r//2)+'R'*(c-1))
    sys.exit(0)
if c % 2 == 1 : 
    print(('D'*(r-1)+'R'+'U'*(r-1)+'R')*(c//2)+'D'*(r-1))
    sys.exit(0)
# 제외할 점 찾기
mini = sys.maxsize
position = [-1,-1]
for i in range(r) : 
    if i % 2 == 0 : 
        for j in range(1,c,2) : 
            if mini > table[i][j] : 
                mini = table[i][j]
                position = [i,j]
    else : 
        for j in range(0,c,2) : 
            if mini > table[i][j] : 
                mini = table[i][j]
                position = [i,j]
if position == [0,1] : 
    print('DR')
    sys.exit(0)
elif position == [1,0] : 
    print('RD')
    sys.exit(0)
ans = ('D'*(r-1)+'R'+'U'*(r-1)+'R') * (position[1] // 2)
if position[0] % 2 == 0 :
    ans += 'RDLD' * (position[0]//2) + 'D' + 'RDLD' * ((r-position[0]-1)//2) + 'RR'
else : 
    ans += 'RDLD' * (position[0]//2) + 'RD' + 'DLDR' * ((r-position[0]-1)//2) + 'R'
ans += ('U' * (r-1)+'R'+'D'*(r-1)+'R') * ((c-position[1]-1)//2)
ans = ans[:-1]
print(ans)