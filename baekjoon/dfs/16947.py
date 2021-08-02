# 서울 지하철 2호선

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def find_cir(li,start) : # 순환하는 가장 긴 리스트 찾기
    global cir
    curr = li[-1]
    flag = True
    for i in dic[curr] : 
        if i not in li : 
            flag = False
            find_cir(li+[i],start)
    if flag and start in dic[curr] : 
        cir =  li

def find_len(curr,cnt) : # 빠져나간 정류장 거리 찾기
    if ans[curr] == 0 : 
        ans[curr] = cnt
        cir.append(curr) # 이미 거리를 구해준 애들은 제외시키기 위함
    for i in dic[curr] : 
        if i not in cir : 
            find_len(i,cnt+1)

input = sys.stdin.readline
N = int(input())
dic = defaultdict()
for _ in range(N) : 
    x,y = map(int,input().split())
    if x in dic.keys() : 
        dic[x].append(y)
    else : 
        dic[x] = [y]
    if y in dic.keys() : 
        dic[y].append(x)
    else : 
        dic[y] = [x]
cir = []
ans = [0 for _ in range(N+1)]
for i in range(1,N+1) : # 순환하는 가장 긴 리스트 찾아서 cir에 넣어줌 길이가 2보다 커야함
    if len(cir) < 3 :  
        find_cir([i],i)
for i in range(1,N+1) : # 순환할 수 있는 애들부터 시작해서 삐져나간 정류장과의 거리를 구해줌
    if i in cir : 
        find_len(i,0)
print(' '.join([str(i) for i in ans[1:]]))