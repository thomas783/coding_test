# Programmers_level_2 삼각 달팽이

def go_down(answer,cur_state,cur_num,sums) : 
    while True : 
        try : 
            if answer[cur_state[0]+1][cur_state[1]] == 0 :
                answer[cur_state[0]+1][cur_state[1]] = cur_num
                cur_num += 1
                cur_state = [cur_state[0]+1,cur_state[1]]
            else : 
                return answer, cur_state, cur_num
            if cur_num == sums : 
                return answer, cur_state, cur_num
        except : 
            return answer, cur_state, cur_num

def go_right(answer,cur_state,cur_num,sums) : 
    while True : 
        try : 
            if answer[cur_state[0]][cur_state[1]+1] == 0 :
                answer[cur_state[0]][cur_state[1]+1] = cur_num
                cur_num += 1
                cur_state = [cur_state[0],cur_state[1]+1]
            else :    
                return answer, cur_state, cur_num
            if cur_num == sums : 
                return answer, cur_state, cur_num
        except : 
            return answer, cur_state, cur_num

def go_up(answer,cur_state,cur_num,sums) : 
    while True : 
        try : 
            if answer[cur_state[0]-1][cur_state[1]-1] == 0 :
                answer[cur_state[0]-1][cur_state[1]-1] = cur_num
                cur_num += 1
                cur_state = [cur_state[0]-1,cur_state[1]-1]
            else : 
                return answer, cur_state, cur_num
            if cur_num == sums : 
                return answer, cur_state, cur_num
        except : 
            return answer, cur_state, cur_num

def solution(n) :
    answer = []
    for i in range(1,n+1) : 
        answer.append([0]*i)
    answer[0][0] = 1 # 시작
    sums = int(n*(n+1)/2)
    cur_num = 2
    cur_state = [0,0]
    while(True) : 
        answer,cur_state,cur_num = go_down(answer,cur_state,cur_num,sums)
        answer,cur_state,cur_num = go_right(answer,cur_state,cur_num,sums)
        answer,cur_state,cur_num = go_up(answer,cur_state,cur_num,sums)
        if cur_num == sums + 1 : 
            break
    result = []
    for i in range(len(answer)) : 
        result += answer[i]
    return result