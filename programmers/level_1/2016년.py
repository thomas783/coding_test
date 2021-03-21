def solution(a, b):
    day = {1:'FRI', 2: 'SAT', 3 : 'SUN', 4: 'MON', 5: 'TUE', 6: 'WED', 0: 'THU'}
    temp = b
    month = [0,31,29,31,30,31,30,31,31,30,31,30]
    for i in range(a) : 
        temp += month[i]
    temp = temp % 7 
    answer = day[temp]
    return answer