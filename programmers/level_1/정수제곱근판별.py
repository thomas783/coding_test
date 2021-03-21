import math
def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)) : 
        answer = (math.sqrt(n)+1)**2
    else : 
        answer = -1
    return answer