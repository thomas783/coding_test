# 큐빙

import sys
def rotate(dir) : 
    T,X,Y,Z,W = U,L,F,R,B
    if dir == 'L' : 
        T,X,Y,Z,W = L,F,U,B,D
    if dir == 'F' : 
        T,X,Y,Z,W = F,U,L,D,R
    if dir == 'R' : 
        T,X,Y,Z,W = R,D,B,U,F
    if dir == 'B' : 
        T,X,Y,Z,W = B,R,D,L,U
    if dir == 'D' : 
        T,X,Y,Z,W = D,B,R,F,L
    T[0][2], T[1][2], T[2][2], T[2][1], T[2][0], T[1][0],\
    T[0][0], T[0][1] = T[0][0], T[0][1], T[0][2], T[1][2],\
    T[2][2], T[2][1], T[2][0], T[1][0]
 
    X[2][2], X[2][1], X[2][0], Y[2][0], Y[1][0], Y[0][0],\
    Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2] = \
    Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], \
    W[0][0], W[0][1], W[0][2], X[2][2], X[2][1], X[2][0]

N = int(input())
# 순서 : 위, 아래, 앞, 뒤, 왼, 오
for _ in range(N) : 
    U = [['w']*3 for _ in range(3)]
    D = [['y']*3 for _ in range(3)]
    F = [['r']*3 for _ in range(3)]
    B = [['o']*3 for _ in range(3)]
    L = [['g']*3 for _ in range(3)]
    R = [['b']*3 for _ in range(3)]
    M = int(input())
    move = list(map(str,sys.stdin.readline().rstrip().split(' ')))
    for dir,r in move : 
        rotate(dir)
        if r == '-' : 
            rotate(dir)
            rotate(dir)
    for i in range(3) : 
        print(''.join(j for j in U[i]))