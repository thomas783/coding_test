# programmers [3차] 파일명 정렬

def solution(li) : 
    answer = []
    for i in range(len(li)) :
        temp_list = list(li[i])
        num = []
        temp = []
        count = 0
        for j in range(len(temp_list)) :
            if temp_list[j].isdigit() :
                if count %2 == 0 :
                    num.append(''.join(temp))
                    temp = []
                    temp.append(temp_list[j])
                    count += 1
                elif count %2 == 1 : 
                    temp.append(temp_list[j])
            else : 
                if count %2 == 0 : 
                    temp.append(temp_list[j])
                elif count %2 == 1 :
                    num.append(''.join(temp))
                    temp = []
                    temp.append(temp_list[j])
                    count += 1
        num.append(''.join(temp))
        answer.append(num)
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(n) for n in answer]