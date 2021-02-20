# 이차원 배열과 연산

def change(A) : # R 연산
    check = False
    if len(A) < len(A[0]) : # C 연산
        check = True
        A = [list(z) for z in zip(*A)]
    new_A = []
    max_val = 0
    for i in A : 
        dic = dict()
        for j in i : 
            if j != 0 :
                if j not in dic.keys() : 
                    dic[j] = 1
                else :
                    dic[j] += 1
        temp = sorted([list(d) for d in dic.items()],key = lambda x : (x[1],x[0]))
        temp_li = []
        for a in temp : 
            temp_li += a
        if len(temp_li) > 100 : 
            temp_li = temp_li[:100]
        new_A.append(temp_li)
        max_val = max(max_val,len(temp_li))
    for i in range(len(new_A)) : 
        for _ in range(max_val-len(new_A[i])) : 
            new_A[i] += [0]
    if check == False : 
        return new_A
    else : # C 연산일 경우 되돌려줌
        new_A = [list(z) for z in zip(*new_A)]
        return new_A
    
import sys
r,c,k = map(int,sys.stdin.readline().rstrip().split(' '))
A = []
for _ in range(3) : 
    A.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
answer = 0
check = False
for _ in range(101) : 
    try :
        if A[r-1][c-1] == k : 
            print(answer)
            check = True
            break
    except : 
        pass
    answer += 1
    A = change(A)
if not check : 
    print(-1)