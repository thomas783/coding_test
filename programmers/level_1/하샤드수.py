# programmers 하샤드 수
def solution(x) : 
    if x % sum(int(n) for n in list(str(x))) == 0 : 
        return True
    else : 
        return False