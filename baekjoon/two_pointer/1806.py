# 부분합

N,S = map(int,input().split())
li = list(map(int,input().split()))
sum_li = [0 for _ in range(N+1)]
for i in range(1,N+1) : 
    sum_li[i] = sum_li[i-1] + li[i-1]
start = 0
end = 1
ans = 100001
while start < N : 
    if sum_li[end] - sum_li[start] < S : 
        if end < N :
            end += 1
        else : 
            start += 1
    else : 
        ans = min(ans,end-start)
        start += 1
if ans == 100001 : 
    print(0)
else : 
    print(ans)