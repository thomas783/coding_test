import sys

input = sys.stdin.readline
N = int(input())
sit = []
for _ in range(N**2) : 
    sit.append(list(map(int,input().split())))
table = [[0 for _ in range(N)] for _ in range(N)]
table[1][1] = sit[0][0]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for s in range(1,N**2) : 
    s_num = sit[s][0]
    can = []
    # 1번 조건
    for x in range(N) : 
        for y in range(N) : 
            if table[x][y] == 0 : 
                count_friend = 0
                count_blank = 0
                for d in range(4) : 
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 1번 조건
                    if 0<=nx<N and 0<=ny<N and table[nx][ny] in sit[s][1:] : 
                        count_friend += 1
                    # 2번 조건
                    elif 0<=nx<N and 0<=ny<N and table[nx][ny] == 0 : 
                        count_blank += 1
                can.append([x,y,count_friend,count_blank])
    # 3번 조건
    can = sorted(can,key = lambda x : (-x[2],-x[3],x[0],x[1]))
    x,y,_,_ = can[0]
    table[x][y] = s_num
sit = sorted(sit,key = lambda x : x[0])
answer = 0
dic = {0:0,1:1,2:10,3:100,4:1000}
for x in range(N) : 
    for y in range(N) : 
        s_num = table[x][y]
        count = 0
        for d in range(4) : 
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and table[nx][ny] in sit[s_num-1][1:] :
                count += 1
        answer += dic[count]
print(answer)
