# 경사로

import sys
def check(road) : 
    road_numbered = []
    cur_height = road[0]
    cur_cnt = 0
    for r in road : 
        if r == cur_height : 
            cur_cnt += 1
        else : 
            road_numbered.append([cur_height,cur_cnt])
            cur_height = r
            cur_cnt = 1
    if cur_cnt != 0 : 
        road_numbered.append([cur_height,cur_cnt])
    if len(road_numbered) == 1 : # 모두 높이가 같은 경우
        return True
    past_height = road_numbered[0][0]
    past_cnt = road_numbered[0][1]
    for i in range(1,len(road_numbered)) : 
        next_height = road_numbered[i][0]
        next_cnt = road_numbered[i][1]
        if abs(past_height - next_height) != 1 : # 높이가 1보다 큰 경우
            return False
        else : 
            if past_height - next_height == 1 : # 왼쪽이 높은 경우
                if next_cnt >= L : 
                    past_height = next_height
                    past_cnt = next_cnt - L
                else : 
                    return False
            elif past_height - next_height == -1 : # 오른쪽이 높은 경우
                if past_cnt >= L : 
                    past_height = next_height
                    past_cnt = next_cnt
                else : 
                    return False
    return True
        

N,L = map(int,sys.stdin.readline().rstrip().split())
maps = []
for _ in range(N) : 
    maps.append(list(map(int,sys.stdin.readline().rstrip().split())))
answer = 0
for m in maps : 
    print(check(m))
    if check(m) :
        answer += 1
maps_transposed = list(map(list,zip(*maps)))
for m in maps_transposed : 
    print(check(m))
    if check(m) : 
        answer += 1
print(answer)
