# 스카이라인

import sys, heapq

n = int(input())
building = []
height = [0 for _ in range(n)]
q = []
# end : 현재 idx번째 건물의 끝나는 지점 저장
end = [0 for _ in range(n)]
# check : 현재까지 끝난 끝점을 저장
check = set()
for i in range(n) : 
    a,b,c = list(map(int,input().split()))
    # 1이면 시작점, -1이면 끝점
    building.append([a,i,1])
    building.append([c,i,-1])
    height[i] = b
    end[i] = c
building = sorted(building,key = lambda x:(x[0],-x[2],-height[x[1]]))
# curr : 현재 높이
curr = 0
ans = []
for i in range(len(building)) :
    # point : 시점, idx : 건물의 인덱스, dir : 시작인지 끝인지 
    point,idx,dir = building[i]
    # 시작점인 경우
    if dir == 1 : 
        if curr < height[idx] : 
            curr = height[idx]
            ans.append([point,curr])
        # 현재 건물의 높이와 끝점을 최대 힙에 저장
        heapq.heappush(q,[-height[idx],end[idx]])
    # 끝점인 경우
    else : 
        # 끝점을 저장
        check.add(point)
        # 최대 높이가 끝난 건물이 아닐때까지 pop
        while q :
            if q[0][1] not in check : 
                break
            heapq.heappop(q)
        # 힙이 비었다면 높이 0으로 초기화
        if not q : 
            if curr : 
                curr = 0
                ans.append([point,curr])
        else : 
            # 힙이 있다면 그 다음으로 높은 건물로 초기화
            if -q[0][0] != curr : 
                curr = -q[0][0]
                ans.append([point,curr])
for i in ans :
    print(i[0],i[1],end=' ')