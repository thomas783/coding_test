# Programmers_level_2_가장 큰 정사각형 찾기

def solution(board):
    for i in range(1,len(board)) : 
        for j in range(1,len(board[i])) : 
            if board[i][j] == 1 : 
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) + 1
    return max([val for row in board for val in row])**2