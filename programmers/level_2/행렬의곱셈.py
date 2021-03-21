# Programmers_level_2_행렬의 곱셈

def solution(arr1,arr2) : 
    new_arr2 = []
    for j in range(len(arr2[0])) : 
        temp = []
        for i in range(len(arr2)) : 
            temp.append(arr2[i][j])
        new_arr2.append(temp)
    li = []
    for i in range(len(arr1)) : 
        temp = []
        for j in range(len(new_arr2)) : 
            temp_list = []
            for k in range(len(new_arr2[j])) : 
                temp_list.append(arr1[i][k] * new_arr2[j][k])
            temp.append(sum(temp_list))
        li.append(temp)
    return li