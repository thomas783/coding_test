# Programmers_level_2_JadenCase 문자열 만들기

def solution(s) :
    answer = ''
    convert = True
    for i in s : 
        if i == ' ' : 
            answer += i
            convert = True
        elif i != ' ' and convert == True : 
            answer += i.upper()
            convert = False
        elif i != ' ' and convert == False : 
            answer += i.lower()
    return answer