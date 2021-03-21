# programmers [1차] 프렌즈4블록

def bomb(li) : 
    bye = set()
    for i in range(len(li)-1) : 
        for j in range(len(li[i])-1) : 
            try :
                if li[i][j] == li[i][j+1] == li[i+1][j] == li[i+1][j+1] :
                    bye.add((i,j))
                    bye.add((i,j+1))
                    bye.add((i+1,j))
                    bye.add((i+1,j+1))
            except : 
                continue
    new_li = []
    for i in range(len(li)) :
        temp = []
        for j in range(len(li[i])) : 
            if (i, j) not in bye : 
                temp.append(li[i][j])
        new_li.append(temp)
    return new_li, len(bye)

def solution(m,n,board) : 
    answer = 0
    board = board[::-1]
    li = []
    for i in range(n) : 
        temp = []
        for j in range(m) :
            temp.append(list(board[j])[i])
        li.append(temp)
    while bomb(li)[1] != 0 : 
        answer += bomb(li)[1]
        li = bomb(li)[0]
    return answer