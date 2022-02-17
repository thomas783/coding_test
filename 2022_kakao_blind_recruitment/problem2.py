# k진수에서 소수 개수 구하기

import math

def is_prime(n) :
    if n < 2 : 
        return False
    for i in range(2,int(math.sqrt(n))+1) : 
        if n % i == 0 : 
            return False 
    else : 
        return True

def change(n,k) : 
    num = ''
    while True : 
        num += str(n % k)
        n = n // k
        if n < k : 
            num += str(n)
            break
    return str(int(num[::-1]))

def solution(n,k) : 
    num = change(n,k)
    num = num.split('0')
    ans = 0
    for i in num : 
        if i != '' and is_prime(int(i)) : 
            ans += 1
    return ans

n = 4
k = 3
print(solution(n,k))