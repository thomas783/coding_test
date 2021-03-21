# Programmers_level_2 [카카오 인턴] 수식 최대화

def solution(expression) : 
    import itertools
    splitted = []
    sign = ['+','-','*']
    rule = [[i,j,k] for i,j,k in itertools.permutations(sign,3)]
    temp = ''
    for ex in expression : 
        if ex not in sign : 
            temp = ''.join([temp,ex])
        else : 
            splitted.append(temp)
            splitted.append(ex)
            temp = ''
    splitted.append(temp)
    answer = []
    for r in rule : 
        temp = splitted.copy()
        for s in r : 
            while s in temp : 
                temp_idx = temp.index(s)
                temp[temp_idx-1] = str(eval(temp[temp_idx-1] + temp[temp_idx] + temp[temp_idx+1]) )
                temp.pop(temp_idx)
                temp.pop(temp_idx)
        answer.append(abs(int(temp[0])))
    return max(answer)