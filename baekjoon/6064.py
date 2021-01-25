# 카잉 달력
def make_calender(M,N,x,y) : 
    if M < N : 
        M,N = N,M
        x,y = y,x
    if y == N : # 나머지가 0인 경우 고려
        y = 0
    for i in range(N) : 
        temp = i * M + x
        if temp % N == y :
            return temp
    return -1 
iter = int(input())
for _ in range(iter) : 
    M, N, x, y = list(map(int,input().split(' ')))
    print(make_calender(M,N,x,y))