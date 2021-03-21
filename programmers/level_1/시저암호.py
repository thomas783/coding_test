def solution(s, n) : 
    reverse = enumerate('abcdefghijklmnopqrstuvwxyz')
    reverse = dict(reverse)
    value = list(reverse.values())
    alpha = dict([(v, k) for k, v in reverse.items()])
    s = list(s)
    temp = []
    for i in s : 
        if i == ' ' : 
                temp.append(' ')
        if i in value : 
            if alpha[i] + n >25 : 
                temp.append(reverse[alpha[i] + n - 26])
            else : 
                temp.append(reverse[alpha[i] + n])
        else:
            if i != ' ' : 
                i = i.lower()
                if alpha[i] + n >25 : 
                    temp.append(reverse[alpha[i] + n - 26].upper())
                else : 
                    temp.append(reverse[alpha[i] + n].upper())
    answer = ''.join(temp[:])
    return answer