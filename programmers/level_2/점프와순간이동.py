# Programmers_level_2_점프와 순간 이동

def solution(N) : 
    count = 0
    while N :
        if N % 2 == 0 : 
            N = N//2
        else : 
            N = N//2
            count += 1
    return count