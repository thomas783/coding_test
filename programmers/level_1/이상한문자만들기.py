# programmers 이상한 문자 만들기
def solution(s) :
    s = s.split(' ')
    for i in range(len(s)) : 
        for j in range(len(s[i])) : 
            temp = list(s[i])
            if j % 2 == 0 :
                temp[j] = temp[j].upper()
            else : 
                temp[j] = temp[j].lower()
            s[i] = ''.join(temp)
    answer = ' '.join(s)
    return answer