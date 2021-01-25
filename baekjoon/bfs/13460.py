# 구슬 탈출 2

import copy
def tilt_left(temp_map) : # 왼쪽으로 기울이는 함수
    maps = copy.deepcopy(temp_map)
    out = []
    for m in range(len(maps)) : 
        for n in range(len(maps[m])) :
            if maps[m][n] == 'B' : 
                a,b = m,n
                while maps[a][b] == 'B' and maps[a][b-1] == '.' : 
                    maps[a][b-1] = 'B'; maps[a][b] = '.'
                    b -= 1
                if maps[a][b-1] == 'O' : 
                    maps[a][b] = '.'
                    out.append('B')
            if maps[m][n] == 'R' : 
                a,b = m,n
                while maps[a][b] == 'R' and maps[a][b-1] == '.' : 
                    maps[a][b-1] = 'R'; maps[a][b] = '.'
                    b -= 1
                if maps[a][b-1] == 'O' :
                    maps[a][b] = '.'
                    out.append('R')
    return maps,out

def tilt_right(temp_map) : # 오른쪽으로 기울이는 함수
    maps = copy.deepcopy(temp_map)
    out = []
    for m in range(len(maps)) : 
        for n in range(len(maps[m])-1,-1,-1) : # 오른쪽으로 미뤄질 수 있게 탐색할 때 오른쪽부터 찾는다.
            if maps[m][n] == 'B' : 
                a,b = m,n
                while maps[a][b] == 'B' and maps[a][b+1] == '.' : 
                    maps[a][b+1] = 'B'; maps[a][b] = '.'
                    b += 1
                if maps[a][b+1] == 'O' : 
                    maps[a][b] = '.'
                    out.append('B')
            if maps[m][n] == 'R' : 
                a,b = m,n
                while maps[a][b] == 'R' and maps[a][b+1] == '.' : 
                    maps[a][b+1] = 'R'; maps[a][b] = '.'
                    b += 1
                if maps[a][b+1] == 'O' :
                    maps[a][b] = '.'
                    out.append('R')
    return maps,out

def tilt_up(temp_map) : # 위쪽으로 기울이는 함수
    maps = copy.deepcopy(temp_map)
    out = []
    for m in range(len(maps)) : 
        for n in range(len(maps[m])) :
            if maps[m][n] == 'B' : 
                a,b = m,n
                while maps[a][b] == 'B' and maps[a-1][b] == '.' : 
                    maps[a-1][b] = 'B'; maps[a][b] = '.'
                    a -= 1
                if maps[a-1][b] == 'O' : 
                    maps[a][b] = '.'
                    out.append('B')
            if maps[m][n] == 'R' : 
                a,b = m,n
                while maps[a][b] == 'R' and maps[a-1][b] == '.' : 
                    maps[a-1][b] = 'R'; maps[a][b] = '.'
                    a -= 1
                if maps[a-1][b] == 'O' :
                    maps[a][b] = '.'
                    out.append('R')
    return maps,out

def tilt_down(temp_map) : # 아래쪽으로 기울이는 함수
    maps = copy.deepcopy(temp_map)
    out = []
    for m in range(len(maps)-1,-1,-1) : 
        for n in range(len(maps[m])) :
            if maps[m][n] == 'B' : 
                a,b = m,n
                while maps[a][b] == 'B' and maps[a+1][b] == '.' : 
                    maps[a+1][b] = 'B'; maps[a][b] = '.'
                    a += 1
                if maps[a+1][b] == 'O' : 
                    maps[a][b] = '.'
                    out.append('B')
            if maps[m][n] == 'R' : 
                a,b = m,n
                while maps[a][b] == 'R' and maps[a+1][b] == '.' : 
                    maps[a+1][b] = 'R'; maps[a][b] = '.'
                    a += 1
                if maps[a+1][b] == 'O' :
                    maps[a][b] = '.'
                    out.append('R')
    return maps,out

M,N = list(map(int,input().split(' '))) # M은 세로길이, N은 가로길이
maze = []
for _ in range(M) : 
    maze.append(list(input()))
queue = [[maze]+[0]]
answer = []
while queue : # bfs
    temp = queue.pop(0)
    temp_map = temp[0]
    temp_val = temp[1]
    if temp_val < 10 :
        temp_left, left_out = tilt_left(temp_map)
        if 'B' in left_out : 
            answer.append(-1)
        else : 
            if 'R' in left_out : 
                answer.append(temp_val+1)
            else :
                if temp_left != temp_map : 
                    queue.append([temp_left]+[temp_val+1])
        temp_right, right_out = tilt_right(temp_map)
        if 'B' in right_out : 
            answer.append(-1)
        else : 
            if 'R' in right_out : 
                answer.append(temp_val+1)
            else :
                if temp_right != temp_map : 
                    queue.append([temp_right]+[temp_val+1])
        temp_up, up_out = tilt_up(temp_map)
        if 'B' in up_out : 
            answer.append(-1)
        else : 
            if 'R' in up_out : 
                answer.append(temp_val+1)
            else :
                if temp_up != temp_map : 
                    queue.append([temp_up]+[temp_val+1])
        temp_down, down_out = tilt_down(temp_map)
        if 'B' in down_out : 
            answer.append(-1)
        else : 
            if 'R' in down_out : 
                answer.append(temp_val+1)
            else :
                if temp_down != temp_map : 
                    queue.append([temp_down]+[temp_val+1])
answer = [i for i in answer if i>0]
if not answer : 
    print(-1)
else : 
    print(min(answer))