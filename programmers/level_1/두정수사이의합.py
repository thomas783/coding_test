def solution(a, b):
    answer = 0
    c = a
    d = b
    if a>b : 
        c = b 
        d = a
    for i in range(c,d+1) : 
        answer += i
    return answer