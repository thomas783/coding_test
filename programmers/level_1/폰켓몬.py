# Programmers_level_2_폰켓몬

def solution(nums) : 
    dic = dict()
    for i in range(len(nums)) : 
        if nums[i] not in dic.keys() : 
            dic[nums[i]] = 1
        else : 
            dic[nums[i]] += 1
    if len(nums)/2 >= len(dic.keys()) : 
        return len(dic.keys())
    else : 
        return len(nums)/2