from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
n = int(input())
box = list(map(int,input().split()))
dic = defaultdict()
for i in range(n) : # 먼저 index마다 비어있는 리스트를 생성
    dic[i] = []
for i in range(n-1) : 
    for j in range(i+1,n) : 
        if box[i] < box[j] :
            dic[i].append(j) # 각 index마다 갈 수 있는 index 담아줌
dp = [0 for _ in range(n)]
ans = 0
for start in range(n) : 
    for curr in dic[start] : 
        dp[curr] = max(dp[curr], dp[start]+1) # 앞에서 쌓아온 길이 그전에 쌓아왔던 길 중 가장 큰것을 넘는지 확인
print(max(dp)+1) # 마지막 박스를 더해줌
