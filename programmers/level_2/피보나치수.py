# Programmers_level_2_피보나치 수

def solution(n) :
    pibo = [0,1]
    for _ in range(n-1) : 
        pibo.append(pibo[-2]+pibo[-1])
    return pibo[-1] % 1234567