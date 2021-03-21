# Programmers_level_2_후보키

def solution(relation) : 
    import itertools
    n = len(relation[0])
    length = len(relation)
    temp_list = list(range(0,n))
    candidate = []
    s = []
    for i in range(1,n+1) : 
        temp = itertools.combinations(temp_list,i)
        candidate.extend(temp)
    for i in candidate : 
        temp_li = []
        for j in range(length) : 
            temp_li2 = []
            for item in i : 
                temp_li2.append(relation[j][item])
            temp_li.append(tuple(temp_li2))
        if len(set(temp_li)) == length : 
            s.append(i)
    final_set = set(s)
    for i in range(len(s)-1) : 
        for j in range(i+1,len(s)) : 
            if set(s[i]) == set(s[i]).intersection(set(s[j])) : 
                final_set.discard(s[j])
    return len(final_set)