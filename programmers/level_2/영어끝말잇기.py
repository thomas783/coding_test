# Programmers_level_2_영어 끝말잇기

def solution(n, words) :
    answer = [0,0]
    done = [words[0]]
    for i in range(1,len(words)) : 
        if words[i][0] == done[-1][-1] and words[i] not in done : 
            done.append(words[i])
        else : 
            if (i+1) % n == 0 :
                answer[0] = n
                answer[1] = (i+1) // n
            else : 
                answer[0] = (i+1) % n
                answer[1] = ((i+1) // n) + 1
            break
    return answer