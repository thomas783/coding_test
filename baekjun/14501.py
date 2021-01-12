from collections import defaultdict
N = int(input())
dic = defaultdict()
days = 0
out = N + 1
for _ in range(N) : 
    days += 1
    dic[days] = list(map(int,input().split(' ')))
answer = 0
queue = [[1] + dic[1] + [0]] 
while queue : 
    temp = queue.pop(0) # temp[0]은 현재 날짜, temp[1,2]는 주어진 시간과 보수, temp[3] 그날까지 총 보수
    for t in range(temp[1],temp[1]+5) : # 그날과 합쳐진 날부터 +5까지 가능한 날을 모두 넣어준다. 
        if temp[0] + t < out :
            queue.append([temp[0] + t] + dic[temp[0] + t] + [temp[2] + temp[3]])    
            answer = max(answer,temp[2] + temp[3])
        elif temp[0] + t == out : 
            answer = max(answer,temp[2] + temp[3])
        else : 
            continue
print(answer)