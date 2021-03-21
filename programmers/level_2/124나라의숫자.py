# programmers level2 -124 나라의 숫자

def solution(num) : 
    change = []
    n = 1
    while num > (3**(n+1)-3)/2 :
        n += 1
    dic = {0:'1',1:'2',2:'4'}
    while n > 0: 
        print(num)
        a = ((3**n)-3)/2
        if num <= a + 3**(n-1) :
            change.append(dic[0])
            num -= 3**(n-1)
        elif a + 3**(n-1) < num and num <= a + 2*3**(n-1) : 
            change.append(dic[1])
            num -= 2*3**(n-1)
        else : 
            change.append(dic[2])
            num -= 3**n
        n -= 1
    answer = ''.join(change)
    return answer