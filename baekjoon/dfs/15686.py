# 치킨 배달

import sys
def dfs(cur_chicken,idx) :
    global ans
    if len(cur_chicken) == M : 
        temp_answer = 0
        for h1,h2 in house : 
            temp = sys.maxsize
            for c1,c2 in cur_chicken : 
                temp = min(temp,abs(h1-c1)+abs(h2-c2))
            temp_answer += temp
        ans = min(ans,temp_answer)
        return
    else : 
        for c in range(idx,len(chicken)) : 
            if chicken[c] in cur_chicken : 
                pass
            else : 
                cur_chicken.append(chicken[c])
                dfs(cur_chicken,c+1)
                cur_chicken.pop()
N,M = map(int,sys.stdin.readline().rstrip().split(' '))
maps = []
for _ in range(N) : 
    maps.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
house = []
chicken = []
for i in range(N) : 
    for j in range(N) : 
        if maps[i][j] == 1 :
            house.append([i,j])
        elif maps[i][j] == 2 : 
            chicken.append([i,j])
ans = sys.maxsize
dfs([],0)
print(ans)
