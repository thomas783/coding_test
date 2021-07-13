# 부분수열의 합
# S의 길이는 1~20, 만들수있는 수의 경우는 2^20-1 메모리 터질우려
# bitmasking 사용

N = int(input())
S = list(map(int,input().split()))
can = set(range(1,2000000))
for bm in range(1,2**N) : 
    temp = 0
    for i in range(N) : 
        if bm & 1 << i :
            temp += S[i]
    if temp in can : 
        can.remove(temp)
print(min(can))