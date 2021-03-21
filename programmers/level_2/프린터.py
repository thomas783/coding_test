# programmers 스택/큐 - 프린터

def solution(priorities, location) : 
    li = []
    temp = list(enumerate(priorities))
    while temp : 
        while temp[0][1] < max(temp, key = lambda x : x[1])[1] : 
            temp = temp[1:] + [temp[0]]
        li.append(temp.pop(0))
    for i, j in li : 
        if i == location : 
            answer = li.index((i,j)) +1
    return answer