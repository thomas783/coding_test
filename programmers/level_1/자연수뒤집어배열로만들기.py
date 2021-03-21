# programmers 자연수 뒤집어 배열로 만들기
def solution(n) : 
    return [int(n) for n in list(str(n))[::-1]]