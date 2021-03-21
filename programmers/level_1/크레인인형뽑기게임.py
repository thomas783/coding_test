# Programmers_level_1_크레인 인형뽑기 게임

def solution(board, moves) : 
    answer = 0
    basket = []
    board = [list(i) for i in zip(*board)]
    for m in moves : 
        for i in range(len(board[m-1])) : 
            if board[m-1][i] == 0 : 
                next
            else : 
                if len(basket) > 0 and basket[-1] == board[m-1][i] : 
                    basket = basket[:-1]
                    answer += 2
                    board[m-1][i] = 0
                    break
                else : 
                    basket.append(board[m-1][i])
                    board[m-1][i] = 0
                    break
    return answer