# 소수의 연속합

def is_prime(n) : 
    li = [True] * (n+1)
    for i in range(2,n+1) : 
        if li[i] == True : 
            j = 2
            while (i*j) <= n : 
                li[i*j] = False
                j+=1
    prime = []
    for i in range(2,n+1) : 
        if li[i] :
            prime.append(i)
    return prime

N = int(input())
li = is_prime(N)
ans = 0
for i in range(len(li)) : 
    tmp = 0
    while tmp < N and i < len(li): 
        tmp += li[i]
        i+= 1
    if tmp == N : 
        ans += 1
print(ans)