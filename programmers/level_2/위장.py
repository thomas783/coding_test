# programmers 해시 - 위장
def solution(clothes):
    clothes = sorted(list(dict(clothes).values()))
    answer = [1]
    for i, j in list(zip(clothes,clothes[1:]+[0])) : 
        if i == j : 
            answer[-1] += 1
        else : 
            answer.append(1)
    answer = answer[:-1]
    for i in range(len(answer)) : 
        answer[i] += 1
    temp_answer = 1
    for i in range(len(answer)) :
        temp_answer = answer[i] * temp_answer
    return temp_answer - 1