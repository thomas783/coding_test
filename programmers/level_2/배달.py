# Programmers_level_3_배달
# 플로이드 와샬

def solution(N, road, K) :
    import sys
    INF = sys.maxsize
    answer = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for i,j,k in road : 
        answer[i][j] = min(k,answer[i][j])
        answer[j][i] = min(k,answer[j][i])
    # 플로이드 워셜 알고리즘 차용
    for k in range(1, N+1) : 
        for i in range(1, N+1) : 
            for j in range(i, N+1) : 
                if i == j : 
                    answer[i][j] = 0
                else : 
                    answer[i][j] = min(answer[i][j], answer[i][k] + answer[k][j])
                    answer[j][i] = min(answer[j][i], answer[j][k] + answer[k][i])
    answer = len([i for i in answer[1] if i <= K])
    return answer