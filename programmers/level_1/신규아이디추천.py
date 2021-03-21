def solution(new_id):
    dic = ['-','_','.']
    for n in range(10) : 
        dic.append(str(n))
    new_id = ''.join([i.lower() for i in new_id]) # 1단계
    new_id = ''.join([i for i in new_id if i in dic or i.isalpha()]) # 2단계
    # 3단계
    flag = True 
    temp = ''
    for i in new_id : 
        if i == '.' and flag : 
            temp += i
            flag = False
        if i != '.' : 
            flag = True
            temp += i
    new_id = temp 
    # 4단계
    if new_id[0] == '.' : 
        new_id = new_id[1:]
    try  : 
        if new_id[-1] == '.' : 
            new_id = new_id[:-1]
    except : 
        pass
    # 5단계
    if new_id == '' : 
        new_id += 'a'
    # 6단계
    if len(new_id) > 15 : 
        new_id = new_id[:15]
        if new_id[-1] == '.' : 
            new_id = new_id[:-1]
    # 7단계
    if len(new_id) < 3 :
        while len(new_id) < 3 : 
            new_id += new_id[-1]
    return new_id

print(solution("abcdefghijklmn.p"))