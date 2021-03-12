# 모노미노도미노 2

import sys
import copy
def push_block(loc,new_block,check) : 
    global answer
    color = copy.deepcopy(new_block)
    flag = True
    while flag : 
        for x,y in loc : 
            if y>5 or color[x][y] != 0 :
                flag = False
                loc = [[x,y-1] for x,y in loc]
                break
        if flag : 
            loc = [[x,y+1] for x,y in loc]
    for x,y in loc : 
        color[x][y] = 1
    # 점수 계산
    color = [list(i) for i in zip(*color)]
    i = 5
    while i>=0 : 
        if sum(color[i]) == 4 : 
            answer += 1
            if i != 5 : 
                color = [[0]*4] + color[:i] + color[i+1:]
            elif i == 5 : 
                color = [[0]*4] + color[:i]
        else : 
            i -= 1
    # 0,1칸에 있는지 확인
    for i in [0,1] : 
        if sum(color[i]) != 0 :
            color = [[0]*4]*(2-i) + color[:4+i]
            break
    color = [list(i) for i in zip(*color)]
    if check : 
        color = [list(i) for i in zip(*color)]
    return color

def set_block(t,x,y,blue,green) :
    loc = [[x,y]]
    if t == 2 : 
        loc.append([x,y+1])
    elif t == 3 : 
        loc.append([x+1,y])
    blue_loc = [[x,i-y] for x,i in loc]
    green_loc = [[i-x,y] for i,y in loc]
    green_loc = [[y,x] for x,y in green_loc]
    green = [list(i) for i in zip(*green)]
    blue = push_block(blue_loc,blue,False)
    green = push_block(green_loc,green,True)
    return blue,green
# input setting
input = sys.stdin.readline
N = int(input())
block = []
for _ in range(N) : 
    block.append(list(map(int,input().split())))
red = [[0 for i in range(4)] for j in range(4)]
blue = [[0 for i in range(6)] for j in range(4)] # 오른쪽
green = [[0 for i in range(4)] for j in range(6)] # 왼쪽
answer = 0
for b in block : 
    t,x,y = b
    blue,green = set_block(t,x,y,blue,green)
block_num = 0
for i in range(4) : 
    for j in range(6) : 
        if blue[i][j] != 0 :
            block_num += 1
        if green[j][i] != 0 : 
            block_num += 1
print(answer)
print(block_num)