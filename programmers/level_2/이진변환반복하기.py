def make_two(i) : 
    answer = ''
    while i > 1 : 
        answer += str(i % 2)
        i = i // 2
    answer += str(i)
    return answer[::-1]

def solution(s):
    cur_len = len(s)
    rep = 0
    zeros = 0
    while len(s) > 1 : 
        rep += 1
        zeros += s.count('0')
        cur_len = len(s) - s.count('0')
        s = make_two(cur_len)
    return [rep,zeros]