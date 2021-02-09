# NMK

import sys

N,M,K = map(int,sys.stdin.readline().split(' '))
if M + K > N + 1 or N > M*K : 
    print(-1)
else : 
    li = list(range(1,N+1))
    g = []
    g.append(0)
    g.append(K)
    N -= K # k를 넣었으니 남은건 n-k
    M -= 1 # 그룹도 m-1
    gs = 1 if M == 0 else N//M
    r = 0 if M == 0 else N%M
    for i in range(M) : 
        g.append(g[-1]+gs+(1 if r > 0 else 0))
        # 나머지의 원소 하나씩 그룹에 더해줌
        if r > 0 : 
            r -= 1 # 하나씩 그룹에 줬으니 빼줌
    for i in range(len(g) - 1) : # 각 그룹을 뒤집어줌
        start = g[i]
        end = g[i+1] - 1
        while start < end : 
            temp = li[start]
            li[start] = li[end]
            li[end] = temp
            start += 1
            end -= 1
    for i in li : 
        print(i, end=' ')