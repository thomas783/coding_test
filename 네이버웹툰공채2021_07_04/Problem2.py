import itertools
def solution(word):
    alpha = ['A','E','I','O','U']
    li = []
    for k in range(1,6) : 
        for i in itertools.product(alpha, repeat=k) : 
            li.append(''.join([j for j in i]))
    li.sort()
    ans = li.index(word) + 1
    return ans