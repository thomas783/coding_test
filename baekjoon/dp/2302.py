import sys

N = int(input())
M = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 2
for i in range(3,N+1) : # 먼저 dp를 만들어준다
    dp[i] = dp[i-1] + dp[i-2] # 두개씩 바꾸는 것이 가능하므로 맨앞의 두개를 기준으로 생각하면 알수있음
if M != 0 : # M이 0인 경우 index error 발생
    vip = []
    for _ in range(M) : 
        vip.append(int(input())-1) # vip를 담아 고정석을 확인
    nofix = []
    count = 0
    for i in range(N) : # vip를 고정시켜을 때 움직일수 있는 자리들의 모임
        if i not in vip : 
            count += 1
        else : 
            nofix.append(count)
            count = 0
    nofix.append(count)
    ans = 1
    for i in nofix :
        if i != 0 : 
            ans *= dp[i]
    print(ans)
else : 
    print(dp[-1])