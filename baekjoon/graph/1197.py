# 최소 스패닝 트리

import sys

def find(x) : 
    if x == arr[x] : 
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x,y) : 
    x = find(x)
    y = find(y)
    if y < x : 
        arr[x] = y
    else : 
        arr[y] = x

input = sys.stdin.readline
v,e = map(int,input().split())
li = []
for _ in range(e) : 
    li.append(list(map(int,input().split())))
li = sorted(li,key = lambda x : x[2])
arr = [i for i in range(v+1)]
ans = 0
for x,y,val in li : 
    if find(x) != find(y) : 
        union(x,y)
        ans += val
print(ans)