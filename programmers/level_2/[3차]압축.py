# Programmers_level_2_[3차] 압축

def solution(msg) : 
    dic = dict([[i,j] for [j,i] in list((enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ',1)))])
    answer = []
    msg = list(msg)[::-1]
    while msg : 
        temp = msg.pop()
        temp_msg = msg.copy()
        iteration = 0
        while temp in dic.keys() :
            iteration += 1
            memory = temp
            try :
                temp += temp_msg.pop()
            except : 
                break
        for _ in range(iteration-1) : 
            msg.pop()
        answer.append(dic[memory])
        dic[temp] = len(dic) + 1
    return answer