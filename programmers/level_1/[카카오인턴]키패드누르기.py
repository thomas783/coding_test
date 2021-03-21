def get_dist(hand, number) : 
    loc = {'1' : (0,0), '2' : (0,1), '3' : (0,2),
          '4' : (1,0), '5' : (1,1), '6' : (1,2),
          '7' : (2,0), '8' : (2,1), '9' : (2,2),
          '*' : (3,0), '0' : (3,1), '#' : (3,2)}
    number = str(number)
    x_hand, y_hand = loc[hand]
    x_num, y_num = loc[number]
    return abs(x_hand - x_num) + abs(y_hand - y_num)

def solution(numbers, hand) : 
    answer = ""
    hand = "R" if hand == "right" else "L"
    left_state = '*'
    right_state = '#'
    for num in numbers :
        if num in [1,4,7] : 
            left_state = str(num)
            answer += "L"
        if num in [3,6,9] : 
            right_state = str(num)
            answer += "R"
        if num in [2,5,8,0] : 
            dis1 = get_dist(left_state,num)
            dis2 = get_dist(right_state,num)
            if dis1 > dis2 : 
                answer += "R"
                right_state = str(num)
            elif dis1 < dis2 : 
                answer += "L"
                left_state = str(num)
            else : 
                answer += hand
                if hand == "R" : 
                    right_state = str(num)
                else : 
                    left_state = str(num)
    return answer