# Programmers_level_2_최솟값 만들기

def solution(A,B) :
    A = sorted(A,reverse = True); B = sorted(B)
    answer = 0
    for i in range(len(A)) : 
        answer += A[i]*B[i]
    return answer