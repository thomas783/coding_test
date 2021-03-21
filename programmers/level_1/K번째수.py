def solution(array, commands) : 
    answer = []
    for i in range(len(commands)) : 
        for a,b,c in [commands[i]] : 
            answer.append(sorted(array[a-1:b])[c-1])
    return answer