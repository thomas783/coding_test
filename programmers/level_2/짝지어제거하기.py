# Programmers_level_2_짝지어 제거하기

def solution(s) : 
    s = list(s)
    new_s = [s.pop()]
    while s : 
        temp1 = s.pop()
        if len(new_s) >0 :
            if new_s[-1] == temp1 :
                new_s.pop()
            else : 
                new_s.append(temp1)
        else : 
            new_s.append(temp1)
    if len(new_s) == 0 :
        return 1
    else :
        return 0