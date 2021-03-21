# programmers 그리디 - 큰 수 만들기

def solution(number,k) : 
    n = len(number) - k
    answer = ['0']
    for i in range(len(number)) : 
        for j in range(len(number)) : 
            if len(answer) != 0 : 
                if int(answer[-1]) < int(number[i]) : 
                    answer.pop()
                    k -= 1
                    if k == -1 : 
                        answer.append(number[i:])
                        break
                else : 
                    answer.append(number[i])
                    break
            else : 
                answer.append(number[i])
                break
        if k == -1 : 
            break
    if len(answer) > n : 
        answer = answer[:n]
    return (''.join(answer))