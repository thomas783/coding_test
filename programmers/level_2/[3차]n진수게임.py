# Programmers_level_2_[3차] n진수 게임

def convert(number,base) : # 먼저 진법을 바꿔주는 재귀함수를 만듬
    T = '0123456789ABCDEF'
    i,j = divmod(number,base)
    if i == 0 : 
        return T[j]
    else : 
        return convert(i,base)+T[j]

def solution(n,t,m,p) : 
    p -= 1
    find = []
    everything = ''
    for i in range(m * t) : 
        everything += convert(i,n)
    for i in range(len(everything)) : 
        if i % m == p : 
            find.append(everything[i])
        if len(find) == t : 
            break
    return ''.join(find)