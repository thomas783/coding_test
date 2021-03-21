# programmers(heap) 더 맵게
import heapq
def solution(scoville, K):
    answer = 0
    count = 0
    scoville = sorted(scoville)
    for i in range(len(scoville)-1) : 
        answer += 1
        temp = heapq.heappop(scoville)
        temp += int(heapq.heappop(scoville))*2
        scoville.append(temp)
        count = scoville[0]
        if count > K : 
            break
    if len(scoville) == 1 :
        if count < K : 
            answer = -1
    return answer