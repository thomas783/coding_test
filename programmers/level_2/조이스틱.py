# programmers 그리디 - 조이스틱

def solution(name) : 
    dic = dict((a,b) for b,a in list(enumerate('BCDEFGHIJKLMN',start = 1)) 
               + list(enumerate('ZYXWVUTSRQPO',start = 1))+ [(0,'A')])
    count = 0
    location = 0
    li = []
    for i in range(len(name)) : 
        count += dic[name[i]]
        if name[i] != 'A' : 
            li.append(i)
    li2 = [n-len(name) for n in li]
    while li : 
        if min(abs(location - li[0]),abs(location - li2[0])) <= min(abs(location - li[-1]),abs(location - li2[-1])) : 
            count += min(abs(location - li[0]),abs(location - li2[0]))
            location = li[0]
            li.pop(0)
            li2.pop(0)
        else : 
            count += min(abs(location - li[-1]),abs(location - li2[-1]))
            location = li[-1]
            li.pop()
            li2.pop()
    return count