# programmers [1차] 다트 게임

def solution(d) : 
    temp_list = []
    d = 't'.join(d.split('10'))
    dic = [str(n) for n in list(range(0,10))] + ['t']
    for i in range(len(d)) : 
        if d[i] in dic : 
            temp_list.append(d[i])
        else : 
            temp_list[-1] = temp_list[-1] + d[i]
    for i in range(len(temp_list)) : 
        for j in range(len(temp_list[i])) : 
            if temp_list[i][j] == '*' : 
                if i == 0 : 
                    temp_list[i] = temp_list[i].replace('*','*2')
                else : 
                    temp_list[i] = temp_list[i].replace('*','*2')
                    temp_list[i-1] = temp_list[i-1] + '*2'
    for i in range(len(temp_list)) : 
        if '#' in temp_list[i] : 
            temp_list[i] = temp_list[i].replace('#','*(-1)')
        if 'S' in temp_list[i] : 
            temp_list[i] = temp_list[i].replace('S','**1')
        if 'D' in temp_list[i] : 
            temp_list[i] = temp_list[i].replace('D','**2')
        if 'T' in temp_list[i] : 
            temp_list[i] = temp_list[i].replace('T','**3')
    for i in range(len(temp_list)) : 
        if 't' in temp_list[i] : 
            temp_list[i] = temp_list[i].replace('t','10')
    answer = 0
    for i in temp_list : 
        answer += eval(i)
    return answer