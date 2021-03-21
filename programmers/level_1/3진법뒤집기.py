def solution(n):
    if n < 3 : 
        return n
    third = ''
    while True : 
        third += str(n % 3)
        n = n // 3
        if n < 3 : 
            third += str(n)
            break
    third = third[::-1]
    answer = int(third[0])
    for i in range(1,len(third)) : 
        answer += int(third[i]) * (3**i)
    return answer