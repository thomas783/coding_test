# programmers 정렬 - H-index

def solution(citations) : 
    n = len(citations)
    answer = 0
    while n != 0 : 
        nonli = [i>=n for i in citations].count(True)
        if nonli >= n : 
            answer = n
            break
        else : 
            n -= 1
    return answer