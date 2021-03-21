# programmers 가운데 글자 가져오기
def solution(s):
    n = len(s)
    if n % 2 == 1 :
        temp = (n + 1) // 2 
        answer = s[temp -1]
    else : 
        temp = n // 2
        answer = s[temp-1:temp+1]
    return answer