# 파괴되지 않은 건물

# 정확도만 통과
# def solution(board,skill) : 
#     for s in skill : 
#         type,r1,c1,r2,c2,degree = s
#         for y in range(r1,r2+1) : 
#             for x in range(c1,c2+1) : 
#                 if type == 1 : 
#                     board[y][x] -= degree
#                 else : 
#                     board[y][x] += degree
#     ans = 0
#     for y in range(len(board)) : 
#         for x in range(len(board[0])) : 
#             if board[y][x] > 0 : 
#                 ans += 1
#     return ans

def solution(board,skill) : 
    tmp_board = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for s in skill : 
        type,r1,c1,r2,c2,degree = s
        if type == 1 : 
            degree = -degree
        tmp_board[r1][c1] += degree
        tmp_board[r2+1][c1] -= degree
        tmp_board[r1][c2+1] -= degree
        tmp_board[r2+1][c2+1] += degree
    for y in range(len(tmp_board)) : 
        for x in range(len(tmp_board[0])-1) : 
            tmp_board[y][x+1] += tmp_board[y][x]
    for x in range(len(tmp_board[0])) : 
        for y in range(len(tmp_board)-1) : 
            tmp_board[y+1][x] += tmp_board[y][x]
    for y in range(len(board)) : 
        for x in range(len(board[0])) : 
            board[y][x] += tmp_board[y][x]
    ans = 0
    for y in range(len(board)) : 
        for x in range(len(board[0])) : 
            if board[y][x] > 0 : 
                ans += 1
    return ans

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board,skill))
