# Programmers_level_2_스킬트리

def solution(skill, skill_trees) : 
    answer = 0
    for t in skill_trees : 
        count = 0
        can = True
        for s in t : 
            if s not in skill : 
                next
            else : 
                if s == skill[count] : 
                    count += 1
                else : 
                    can = False
                    break
        if can : 
            answer += 1
    return answer