# Programmers_level_3_괄호 변환

def check(p) : # 올바른 괄호 문자열인지 체크
    length1 = len(p)
    while p : 
        p = p.replace('()','')
        length2 = len(p)
        if length1 == length2 : 
            return False
        else : 
            length1 = len(p)
    return True

def change(p) : 
    if p == '(' : 
        return ')'
    else : 
        return '('

def split_uv(p) : 
    for i in range(1,len(p)+1) : # u와 v로 분리
        if p[:i].count('(') == p[:i].count(')') : 
            u = p[:i]
            v = p[i:]
            return u, v

def solution(p) :
    answer = ''
    if check(p) : 
        return p
    u,v = split_uv(p)
    if check(u) : 
        answer += u + solution(v)
    else : 
        u = ''.join([change(i) for i in u[1:-1]])
        v = '(' + solution(v) + ')'
        answer += v + u
    return answer