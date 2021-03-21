# programmers 예산
def solution(d, budget) : 
    d = sorted(d)
    sum = 0
    answer = 0
    for i in range(len(d)) :
        sum += d[i]
        if sum <= budget : 
            answer += 1
    return answer