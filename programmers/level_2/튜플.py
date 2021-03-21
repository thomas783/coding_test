# Programmers_level_2_튜플

def solution(s) : 
    s = s[:-2].replace('{','').split('},')
    s.sort(key = lambda x: len(x))
    li = []
    for i in range(len(s)) : 
        temp = []
        temp_li = s[i].split(',')
        for j in temp_li : 
            temp.append(int(j))
        li.append(temp)
    answer = []
    for i in range(len(li)) : 
        for j in li[i] : 
            if j not in answer  :
                answer.append(j)
    return answer