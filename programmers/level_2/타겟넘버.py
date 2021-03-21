# Programmers 깊이/너비 우선탐색 - 타겟 넘버

def solution(numbers, target) : 
    case1 = [numbers[0]]
    for i in range(1,len(numbers)) : 
        temp_list = []
        for j in case1 : 
            temp_list.append(j + numbers[i])
            temp_list.append(j - numbers[i])
        case1 = temp_list.copy()
    case2 = [n-numbers[0]*2 for n in case1]
    case1.extend(case2)
    answer = 0
    for i in range(len(case1)) :
        if target == case1[i] : 
            answer += 1
    return answer