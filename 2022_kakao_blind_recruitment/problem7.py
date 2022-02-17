# 사라지는 발판

from copy import deepcopy

def aturn(board,aloc,bloc,cnt) : 
    if board[aloc[0]][aloc[1]] == 0 :
        return (True,cnt)
    flag = True
    winner = []
    loser = []
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    for d in range(4) : 
        ny = aloc[0] + dy[d]
        nx = aloc[1] + dx[d]
        if 0<=ny<len(board) and 0<=nx<len(board[0]) and board[ny][nx] == 1 :
            flag = False
            tmp = deepcopy(board)
            tmp[aloc[0]][aloc[1]] = 0
            is_win,next_cnt = bturn(tmp,[ny,nx],bloc,cnt+1)
            if is_win : 
                winner.append(next_cnt)
            else : 
                loser.append(next_cnt)
    if flag : 
        return (True,cnt)
    else : 
        if winner :
            return (False,min(winner))
        else : 
            return (True,max(loser))

def bturn(board,aloc,bloc,cnt) : 
    if board[bloc[0]][bloc[1]] == 0 :
        return (True,cnt)
    flag = True
    winner = []
    loser = []
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    for d in range(4) : 
        ny = bloc[0] + dy[d]
        nx = bloc[1] + dx[d]
        if 0<=ny<len(board) and 0<=nx<len(board[0]) and board[ny][nx] == 1 :
            flag = False
            tmp = deepcopy(board)
            tmp[bloc[0]][bloc[1]] = 0
            is_win,next_cnt = aturn(tmp,aloc,[ny,nx],cnt+1)
            if is_win : 
                winner.append(next_cnt)
            else : 
                loser.append(next_cnt)
    if flag : 
        return (True,cnt)
    else : 
        if winner :
            return (False,min(winner))
        else : 
            return (True,max(loser))

def solution(board,aloc,bloc) : 
    answer = aturn(board,aloc,bloc,0)[1]
    return answer

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1,0]
bloc = [1,2]
print(solution(board,aloc,bloc))