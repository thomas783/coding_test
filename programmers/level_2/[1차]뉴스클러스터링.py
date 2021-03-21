# Programmers_level_2_[1차] 뉴스 클러스터링

def solution(str1,str2) :
    str1 = str1.lower()
    str2 = str2.lower()
    temp1 = []
    temp2 = []
    for i in range(len(str1)-1) : 
        if (str1[i] + str1[i+1]).isalpha() : 
            temp1.append(str1[i]+str1[i+1])
    for j in range(len(str2)-1) : 
        if (str2[j] + str2[j+1]).isalpha() : 
            temp2.append(str2[j]+str2[j+1])
    if len(temp1) == 0 and len(temp2) == 0 : 
        return 65536
    str1_dict = dict()
    str2_dict = dict()
    for i in temp1 : 
        if i not in str1_dict.keys() : 
            str1_dict[i] = 1
        else : 
            str1_dict[i] += 1
    for i in temp2 : 
        if i not in str2_dict.keys() : 
            str2_dict[i] = 1
        else : 
            str2_dict[i] += 1
    inter = dict()
    union = dict()
    for i,j in str1_dict.items() : 
        if i in str2_dict.keys() : 
            if j >= str2_dict[i] : 
                inter[i] = str2_dict[i]
                union[i] = j
            else : 
                inter[i] = j
                union[i] = str2_dict[i]
        else : 
            union[i] = j
    for i,j in str2_dict.items() : 
        if i not in union.keys() : 
            union[i] = j
    inter = sum(inter.values())
    union = sum(union.values())
    return int(inter/union * 65536)