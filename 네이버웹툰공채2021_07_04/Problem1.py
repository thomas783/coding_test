def solution(S, pattern):
    dic = dict()
    for p in pattern : 
        if p not in dic.keys() : 
            dic[p] = 1
        else : 
            dic[p] += 1
    patt = [[i,j] for i,j in dic.items()]
    alpha = [i for i in dic.keys()]
    count = 0
    for i in range(len(S)-len(pattern)+1) :
        if i != len(S) - len(pattern) : 
            temp = S[i:i+len(pattern)]
        else : 
            temp = S[i:]
        flag = True
        for a in alpha : 
            if temp.count(a) != dic[a] : 
                flag = False
        if flag : 
            count += 1
    return count