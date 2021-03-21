# Programmers_level_2_[3차] 방금 그곡

def solution(m, musicinfos) : 
    for i in range(len(m)) : 
        if m[i] == '#' : 
            m = m[:i-1] + m[i-1].lower() + m[i:]
    m = m.replace('#','')
    new_li = []
    for i in musicinfos : 
        new_li.append(i.split(','))
    new = []
    for i in range(len(new_li)) : 
        for j in range(len(new_li[i][3])) : 
            if new_li[i][3][j] == '#' : 
                new_li[i][3] = new_li[i][3][:j-1] + new_li[i][3][j-1].lower() + new_li[i][3][j:]
        new_li[i][3] = new_li[i][3].replace('#','')
    for i in range(len(new_li)) : 
        temp = []
        temp.append(new_li[i][2])
        t = int(new_li[i][1][:2]) * 60 + int(new_li[i][1][-2:]) - int(new_li[i][0][:2]) * 60 - int(new_li[i][0][-2:])
        j = t // len(new_li[i][3]); k = t % len(new_li[i][3])
        temp.append(str(new_li[i][3]) * j + str(new_li[i][3])[:k])
        temp.append(t)
        new.append(temp)
    answer = [0,0]
    for i in range(len(new)) : 
        if m in new[i][1] and answer[1] < new[i][2] : 
            answer[0] = new[i][0]
            answer[1] = new[i][2]
    if answer[0] == 0 :
        return '(None)'
    else : 
        return answer[0]