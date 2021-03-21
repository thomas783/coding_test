# programmers 완전탐색 - 모의고사

def solution(answers) : 
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thi = [3,3,1,1,2,2,4,4,5,5]
    count = [0] * 3
    answer = []
    for i in range(len(answers)) : 
        if answers[i] == fir[i%5] : 
            count[0] += 1
        if answers[i] == sec[i%8] : 
            count[1] += 1
        if answers[i] == thi[i%10] : 
            count[2] += 1
    for i in range(len(count)) : 
        if count[i] == max(count) : 
            answer.append(i+1)
    return answer