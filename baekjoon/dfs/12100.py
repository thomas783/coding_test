# 2048(easy)

import sys
import copy
def push(maps,N,dir,itr) : 
    temp_maps = copy.deepcopy(maps)
    if dir == 0 : # 위로 미는 경우
        for j in range(N) : 
            idx = 0
            for i in range(1,N) :
                if temp_maps[i][j] : 
                    temp = temp_maps[i][j]
                    temp_maps[i][j] = 0
                    if temp_maps[idx][j] == 0 : 
                        temp_maps[idx][j] = temp
                    elif temp_maps[idx][j] == temp :
                        temp_maps[idx][j] = temp * 2
                        idx += 1
                    else : 
                        idx += 1
                        temp_maps[idx][j] = temp
    elif dir == 1 : # 아래로 미는 경우
        for j in range(N) : 
            idx = N-1
            for i in range(N-2,-1,-1) : 
                if temp_maps[i][j] : 
                    temp = temp_maps[i][j]
                    temp_maps[i][j] = 0
                    if temp_maps[idx][j] == 0 : 
                        temp_maps[idx][j] = temp
                    elif temp_maps[idx][j] == temp : 
                        temp_maps[idx][j] = temp * 2
                        idx -= 1
                    else :
                        idx -= 1
                        temp_maps[idx][j] = temp
    elif dir == 2 : # 왼쪽으로 미는 경우
        for i in range(N) : 
            idx = 0
            for j in range(1,N) : 
                if temp_maps[i][j] : 
                    temp = temp_maps[i][j]
                    temp_maps[i][j] = 0
                    if temp_maps[i][idx] == 0 : 
                        temp_maps[i][idx] = temp
                    elif temp_maps[i][idx] == temp : 
                        temp_maps[i][idx] = temp * 2
                        idx += 1
                    else : 
                        idx += 1
                        temp_maps[i][idx] = temp
    else : # 오른쪽으로 미는 경우
        for i in range(N) : 
            idx = N - 1
            for j in range(N-2,-1,-1) :
                if temp_maps[i][j] : 
                    temp = temp_maps[i][j]
                    temp_maps[i][j] = 0
                    if temp_maps[i][idx] == 0 : 
                        temp_maps[i][idx] = temp
                    elif temp_maps[i][idx] == temp : 
                        temp_maps[i][idx] = temp * 2
                        idx -= 1
                    else : 
                        idx -= 1
                        temp_maps[i][idx] = temp
    return [temp_maps,itr+1]

N = int(input())
maps = []
for _ in range(N) : 
    maps.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
queue = [[maps,0]]
answer = 0
while queue : 
    temp = queue.pop(0)
    new_map = temp[0]
    itr = temp[1]
    if itr == 5 : 
        for i in range(N) : 
            for j in range(N) : 
                answer = max(answer,new_map[i][j])
    else : 
        for i in range(4) : 
            queue.append(push(new_map,N,i,itr))
print(answer)