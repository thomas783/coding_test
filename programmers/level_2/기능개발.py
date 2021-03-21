# programmers 스택/큐 - 기능개발

def solution(progresses, speeds) : 
    answer = []
    for i, j in zip(progresses,speeds) :
        temp_val = 0
        while i<100 : 
            temp_val += 1
            i += j
        answer.append(temp_val)
    answer = answer[::-1]
    real_answer = []
    while answer != [] : 
        temp = answer.pop()
        temp_val = 1
        for i in range(len(answer)) : 
            if answer[-1] <= temp : 
                temp_val += 1
                answer.pop()
        real_answer.append(temp_val)
    return real_answer