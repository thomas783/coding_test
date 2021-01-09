def lcm(a,b) : # 마지막 해는 두 수의 최소공배수
    lcm = a * b
    if a < b : 
        a,b = b,a
    while(b) : 
        a,b = b,a%b
    lcm = lcm//(a)
    return lcm
iter = int(input())
for _ in range(iter) : 
    M, N, x, y = list(map(int,input().split(' ')))
    first = 0; second = 0
    answer = 0
    for i in range(lcm(M,N)) : 
        if first < M : 
            first += 1
        else : 
            first = 1
        if second < N : 
            second += 1
        else : 
            second = 1
        answer += 1
        if first == x and second == y : 
            print(answer)
            break
        else : 
            continue
    if answer == lcm(M,N) : 
        print(-1)
