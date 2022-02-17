# 양과 늑대

from collections import deque

def solution(info,edges) : 
    graph = [[] for _ in range(len(info))]
    for i,j in edges : 
        graph[i].append(j)
    deq = deque()
    deq.append([graph[0],1,0])
    ans = 0
    while deq : 
        curr,sheep,wolf = deq.popleft()
        if not curr or sheep <= wolf : 
            ans = max(ans,sheep)
            continue
        for c in curr : 
            idx = curr.index(c)
            curr.remove(c)
            tmp = curr + graph[c]
            if info[c] == 0 : 
                deq.append([tmp,sheep+1,wolf])
            else : 
                deq.append([tmp,sheep,wolf+1])
            curr.insert(idx,c)
    return ans

info = [0 for _ in range(12)]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info,edges))