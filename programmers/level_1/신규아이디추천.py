def solution(new_id):
    dic = ['-','_','.']
    for n in range(10) : 
        dic.append(str(n))
    new_id = ''.join([i.lower() for i in new_id]) # 1단계
    new_id = ''.join([i for i in new_id if i in dic or i.isalpha()]) # 2단계
    new_id = 
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))