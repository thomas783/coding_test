# programmers 그리디 - 구명보트

def solution(people, limit) :
    couple = 0
    people.sort()
    min = 0; max = len(people) - 1
    while min < max :
        if people[min] + people[max] <= limit : 
            min += 1; max -= 1; couple += 1
        else : 
            max -= 1
    return len(people) - couple