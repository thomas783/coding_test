# programmers 완전탐색 - 카펫

def solution(brown, red) : 
    br = brown + red
    candidate = []
    for i in range(2, br) : 
        if br % i == 0 : 
            if i >= int(br/i) : 
                candidate.append([i, int(br/i)])
    inner = []
    for i in range(1, red+1) : 
        if red % i == 0 : 
            if i >= int(red/i) : 
                inner.append([i, int(red/i)])
    for x,y in candidate : 
        for z, k in inner : 
            if x-z == 2 and y - k == 2 : 
                answer = [x,y]
    return answer