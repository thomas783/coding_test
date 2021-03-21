def solution(s):
    temp = []
    for i in range(len(s)) :
        temp.append(s[i])
    temp = sorted(temp,reverse = True)
    temp_list = ''
    for i in range(len(temp)) :
        temp_list += temp[i]
    return temp_list