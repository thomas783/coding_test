# Programmers_level_2_[1차] 캐시

def solution(c,cities) : 
    if c == 0 : 
        return len(cities) * 5
    answer = 0
    cities = cities[::-1]
    for i in range(len(cities)) : 
        cities[i] = cities[i].lower()
    recent = list(range(c))
    page = [0] * c
    while cities : 
        temp = cities.pop()
        if temp not in page : 
            page[recent[0]] = temp
            recent = recent[1:] + [page.index(temp)]
            answer += 5
        else : 
            recent.remove(page.index(temp))
            recent += [page.index(temp)]
            answer += 1
    return answer