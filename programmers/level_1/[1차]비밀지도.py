# programmers [1차] 비밀지도

def solution(n,arr1,arr2) :
    temp_list = []
    for i,j in zip(arr1,arr2) : 
        zeros = [str(0)]*n
        temp_val = bin(i|j)[2:]
        if len(temp_val) < n : 
            temp_val = ''.join((zeros + list(temp_val))[-n:])
        temp_val = temp_val.replace('1','#').replace('0',' ')
        temp_list.append(temp_val)
    return temp_list