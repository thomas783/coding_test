def solution(N, stages):
    dic = {}
    n = len(stages)
    for i in range(1,N+1):
        if stages.count(i) == 0 : 
            dic[i] = 0 
            continue
        item = stages.count(i)/n
        n-=stages.count(i)
        dic[i] = item
    return sorted(dic, key=lambda k : dic[k], reverse = True)