# programmers 완전탐색 - 소수 찾기
def is_prime(n) : 
    answer = True
    if n > 1 : 
        for i in range(2, int(n/2+1)) : 
            if n%i == 0 : 
                answer = False
                break
            answer = True
    else : 
        answer = False
    return answer

def make_list(str) : 
    import itertools
    li = []
    for i in range(1,8) : 
        temp = [int(''.join(i)) for i in itertools.permutations(str,i)]
        li.extend(temp)
    return set(li)

def solution(numbers) :
    temp = make_list(numbers)
    answer = 0
    for i in temp : 
        if is_prime(i) : 
            answer += 1
    return answer