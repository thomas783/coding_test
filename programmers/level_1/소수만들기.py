# Programmers_level_2_소수 만들기

def is_prime(n) : 
    if n > 1 : 
        for i in range(2,n) : 
            if n%i == 0 : 
                return False
    else : 
        return False
    return True

def solution(nums) : 
    import itertools
    li = [sum(i) for i in itertools.combinations(nums,3)]
    answer = 0
    for i in li : 
        if is_prime(i) : 
            answer += 1
    return answer