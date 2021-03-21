def check_box(piece) :
    num = piece[0][0]
    for i in range(len(piece)) : 
        for j in range(len(piece)) : 
            if piece[i][j] != num : 
                return False
    return True

def split_four(piece) : 
    first = []
    second = []
    third = []
    fourth = []
    cur_stage = int(len(piece)/2) 
    for i in range(cur_stage) : 
        first.append(piece[i][:cur_stage])
        second.append(piece[i][cur_stage:])
    for j in range(cur_stage,len(piece)) : 
        third.append(piece[j][:cur_stage])
        fourth.append(piece[j][cur_stage:])
    return [first,second,third,fourth]

def solution(arr) : 
    zeros = 0
    ones = 0
    pieces = [arr]
    while len(pieces) > 0 : 
        piece = pieces.pop(0)
        if len(piece) < 2 : 
            if piece[0][0] == 1 : 
                ones += 1
            else : 
                zeros += 1
        else : 
            if check_box(piece) == True :
                if piece[0][0] == 1 : 
                    ones += 1
                else : 
                    zeros += 1
            else: 
                pieces += split_four(piece)
    return [zeros,ones]