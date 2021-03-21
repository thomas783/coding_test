# Programmers_level_2_다음 큰 숫자

def solution(n) : 
    curr = bin(n)[2:]
    next_ = n
    while True : 
        next_ += 1
        if curr.count('1') == bin(next_)[2:].count('1') : 
            return next_