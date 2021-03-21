# programmers 정렬 - 가장 큰 수

def solution(numbers) : 
    answer = [0]*len(numbers)
    numbers = [str(i) for i in numbers]
    answer = ''.join(sorted(numbers, key = lambda x: (x[0],x[1%len(x)], x[2%len(x)],x[3%len(x)]), reverse = True))
    # 첫째자리 기준, 둘째자리 기준, 셋째자리 기준, 넷짜자리 기준으로 정렬
    if int(answer) == 0 : 
        answer = '0'
    return answer