# 수들의 합 2
# pypy3으로 뚫림

N,M = map(int,input().split())
li = list(map(int,input().split()))
ans = 0
for i in range(N) : 
    temp = 0
    for j in range(i,N) : 
        temp += li[j]
        if temp == M :
            ans += 1
        elif temp > M : 
            break
print(ans)