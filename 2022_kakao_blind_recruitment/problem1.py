# 신고 결과 받기

def solution(id_list, report, k) : 
    li = [set() for _ in range(len(id_list))]
    for r in report : 
        start,end = r.split()
        li[id_list.index(start)].add(end)
    dic = dict()
    for i in li : 
        for j in i : 
            if j in dic : 
                dic[j] += 1
            else : 
                dic[j] = 1
    exit = set()
    for a,b in dic.items() : 
        if b >= k : 
            exit.add(a)
    answer = [0 for _ in range(len(id_list))]
    for i in range(len(id_list)) : 
        for j in li[i] : 
            if j in exit : 
                answer[i] += 1
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list,report,k))