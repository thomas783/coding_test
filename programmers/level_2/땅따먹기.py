# Programmers_level_2_땅따먹기

def solution(land) :
    answer = land.copy()
    for i in range(len(land)-1) : 
        temp = land[i]
        for j in range(len(land[0])) : 
            answer[i+1][j] = answer[i+1][j] + max(temp[:j] + temp[j+1:])
    return max(answer[-1])