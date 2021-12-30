# 카카오 상반기 인턴 코테 2번

def check(table) :
    dx = [-1,-1,-1,0,1,1,1,0,-2,0,2,0]
    dy = [-1,0,1,1,1,0,-1,-1,0,2,0,-2]
    for i in range(len(table)) : 
        for j in range(len(table)) : 
            if table[i][j] == 'P' : 
                for d in range(12) :  
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<5 and 0<=ny<5 and table[nx][ny] == 'P' :
                        if d in [1,3,5,7] : # 맨해튼 거리가 1인 경우
                            return 0
                        elif d == 0 : 
                            if table[i-1][j] == 'O' or table[i][j-1] == 'O' : 
                                return 0
                        elif d == 2 : 
                            if table[i-1][j] == 'O' or table[i][j+1] == 'O' : 
                                return 0
                        elif d == 4 : 
                            if table[i+1][j] == 'O' or table[i][j+1] == 'O' : 
                                return 0
                        elif d == 6 : 
                            if table[i+1][j] == 'O' or table[i][j-1] == 'O' : 
                                return 0
                        elif d == 8 : 
                            if table[i-1][j] == 'O' :
                                return 0
                        elif d == 9 : 
                            if table[i][j+1] == 'O' :
                                return 0
                        elif d == 10 : 
                            if table[i+1][j] == 'O' : 
                                return 0
                        elif d == 11 : 
                            if table[i][j-1] == 'O' : 
                                return 0
    return 1

def solution(places) :
    answer = []
    for i in range(len(places)) : 
        table = []
        for j in places[i] : 
            table.append(list(j))
        answer.append(check(table))
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
