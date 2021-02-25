# 게리맨더링 2

def check(x,y,d1,d2) :
    one,two,three,four,five = 0,0,0,0,0
    temp = [[0] * (N+1) for i in range(N+1)] # 5번 구역을 담아줌
    for i in range(d1+1) : 
        temp[x+i][y-i] = 5
        temp[x+d2+i][y+d2-i] = 5
    for i in range(d2+1) :
        temp[x+i][y+i] = 5
        temp[x+d1+i][y-d1+i] = 5
    for i in range(x+1,x+d1+d2) :
        isTrue = False
        for j in range(1,N+1) : 
            if temp[i][j] == 5 : 
                isTrue = not isTrue
            if isTrue : 
                temp[i][j] = 5
    for i in range(1,N+1) : 
        for j in range(1,N+1) : 
            if temp[i][j] == 5 : 
                five += area[i][j]
            else : 
                if 1<=i<x+d1 and 1<=j<=y : 
                    one += area[i][j]
                elif 1<=i<=x+d2 and y<j<=N : 
                    two += area[i][j]
                elif x+d1<=i<=N and 1<=j<y-d1+d2 : 
                    three += area[i][j]
                elif x+d2<i<=N and y-d1+d2<=j<=N :
                    four += area[i][j]
    answer = [one,two,three,four,five]
    return max(answer) - min(answer)

import sys
N = int(input())
area = [[]]
for _ in range(N) : 
    area.append([0] + list(map(int,sys.stdin.readline().rstrip().split())))
answer = sys.maxsize
for x in range(1,N+1) : 
    for y in range(1,N+1) : 
        for d1 in range(1,N+1) : 
            for d2 in range(1,N+1) : 
                if 1<=x<x+d1+d2<=N and 1<=y-d1<y<y+d2<=N : 
                    answer = min(answer,check(x,y,d1,d2))
print(answer)
