def solution(n, lost, reverse) : 
    answer = 0
    temp = [1] * n
    temp.insert(0,1000)
    temp.append(1000)
    for i in lost : 
        temp[i] = 0
    a= []
    for j in reverse : 
        if temp[j] == 0 :
            temp[j] = 1
        else:
            a.append(j)
    for j in a :
        if temp[j - 1] == 0 :
            temp[j - 1] = 1
        elif temp[j + 1] == 0 :
            temp[j +1] = 1  
    temp = temp[1:-1]
    answer = sum(temp)
    return answer