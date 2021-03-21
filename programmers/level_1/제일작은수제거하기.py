# programmers 제일 작은 수 제거하기
def solution(arr) :
    if len(arr) !=1 :
        arr.remove(min(arr))
        answer = arr
    else : 
        answer = [-1]
    return answer