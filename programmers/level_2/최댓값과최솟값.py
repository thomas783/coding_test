# Programmers_level_2_최댓값과 최솟값

def solution(s) :
    return ' '.join([str(min([int(x) for x in s.split(' ')])),str(max([int(x) for x in s.split(' ')]))])