# Programmers_level_2_예상 대진표

def solution(n,a,b) :
    answer = 0
    a,b = min(a,b), max(a,b)
    while True: 
        if abs(a - b) == 1 and a % 2 == 1 and b % 2 == 0 : 
            break
        answer += 1
        a = a//2 + a % 2
        b = b//2 + b % 2
    return answer + 1