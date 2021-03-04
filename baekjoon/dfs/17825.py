# 주사위 윷놀이

import sys
def dfs(idx,temp_answer) : 
    global answer
    if idx == 10 : 
        answer = max(answer,temp_answer)
        return
    for i in range(4) : 
        x, x_init, move = horse[i],horse[i],moves[idx]
        if x == 5 or x == 10 or x == 15 : 
            x = change[x]
            move -= 1
        if x + move <= 21 : 
            x += move
        else : 
            for _ in range(move) : 
                x = a[x]
        if c[x] and x != 21 : 
            continue
        c[x_init], c[x], horse[i] = 0,1,x
        dfs(idx+1,temp_answer + add[x])
        c[x_init], c[x], horse[i] = 1,0,x_init

input = sys.stdin.readline
moves = list(map(int,input().split()))
a = [0 for i in range(33)] # 윷놀이판
for i in range(21) : 
    a[i] = i+1
a[21] = 21
a[22],a[23],a[24] = 23,24,30
a[25],a[26] = 26, 30
a[27],a[28],a[29] = 28,29,30
a[30],a[31],a[32] = 31,32,20
change = [0 for _ in range(16)]
change[5],change[10],change[15] = 22,25,27
add = [0 for _ in range(33)]
for i in range(21) : 
    add[i] = i*2
add[22],add[23],add[24] = 13,16,19
add[25],add[26] = 22,24
add[27],add[28],add[29] = 28,27,26
add[30],add[31],add[32] = 25,30,35
horse = [0,0,0,0]
c = [0 for _ in range(33)]
answer = 0
dfs(0,0)
print(answer)