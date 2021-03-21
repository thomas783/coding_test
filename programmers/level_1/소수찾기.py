def solution(n) : 
    prime = set(range(2,n+1))
    for i in range(2, n+1) :
        if i in prime : 
            prime -= set(i for i in range(i*2, n+1,i))
    return len(prime)