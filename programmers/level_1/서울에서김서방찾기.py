def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            num = i
    answer = '김서방은 {}에 있다'.format(num)
    return answer