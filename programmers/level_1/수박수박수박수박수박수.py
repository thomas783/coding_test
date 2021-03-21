def solution(n):
    answer = ''
    su = '수'
    bak = '박'
    for i in range(n):
        if i%2 == 0 :
            answer += su
        else : 
            answer += bak
    return answer