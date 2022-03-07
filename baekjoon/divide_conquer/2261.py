# 가장 가까운 두 점

import sys

def get_dist(p1,p2) :
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def func(start,end) : 
    # 점이 하나라면 최대값 리턴
    if start == end : 
        return float('inf')
    # 점이 두개라면 해당 거리 리턴
    if end - start == 1 : 
        return get_dist(li[start],li[end])
    mid = (start+end)//2
    mindist = min(func(start,mid),func(mid,end))
    # x축을 기준으로 후보 점 찾기
    target = []
    for i in range(start,end+1) : 
        if (li[mid][0]-li[i][0])**2 < mindist : 
            target.append(li[i])
    # y축 기준으로 정렬
    target = sorted(target,key=lambda x:x[1])
    # y축 기준으로 두 점들 거리 비교
    for i in range(len(target)-1) :
        for j in range(i+1,len(target)) : 
            if (target[i][1] - target[j][1])**2 < mindist : 
                mindist = min(mindist,get_dist(target[i],target[j]))
            else :
                break
    return mindist

n = int(input())
li = []
for _ in range(n) : 
    li.append(list(map(int,input().split())))
li = sorted(li)
print(func(0,n-1))