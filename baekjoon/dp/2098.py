# 모르겠어서 답지 참고
# bitmasking과 dp 사용
import sys
N = int(input())
W = []
INF = sys.maxsize
for _ in range(N) : 
    W.append(list(map(int,input().split())))
dp = [[None] * (1<<N) for _ in range(N)]
def find_path(last,visited) : # 현재위치
    if visited == (1<<N) -1 : # 모두 순회했을시
        return W[last][0] or INF # 원래 위치로 돌아가는 방법 return 없으면 INF return
    if dp[last][visited] is not None : # 이미 계산되어 있다면
        return dp[last][visited]
    tmp = INF
    for city in range(N) : 
        if visited & (1 << city) == 0 and W[last][city] != 0 : 
            tmp = min(tmp,find_path(city,visited | (1 << city)) + W[last][city])
    dp[last][visited] = tmp
    return tmp
print(find_path(0,1<<0))