# Programmers_level_2_숫자의 표현

def solution(n) :
    answer = 1 # 자기자신 무조건 가능
    if n % 2 == 1 : 
        answer += 1 # 홀수면 두개로 무조건 나누기 가능
        for i in range(3,int(n/2)) : 
            if n % i == 0 : 
                temp_val = n / i
                if temp_val % 2 == 1: 
                    answer += 1
    else : 
        for i in range(2, int(n/2)) : 
            if n % i == 0 : 
                temp_val = n / i
                if temp_val % 2 == 1 : 
                    answer += 1
    return answer