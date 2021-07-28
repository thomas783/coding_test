# 단어 수학

N = int(input())
li = []
for _ in range(N) : 
    li.append(input())
alpha = set()
for i in li : 
    for j in i : 
        alpha.add(j)
alpha = list(alpha)
dic = dict(zip(alpha,[0 for _ in range(len(alpha))]))
for i in li : 
    for j in range(len(i)) : 
        dic[i[::-1][j]] += 10 ** j
temp = zip(sorted(dic.values(),reverse=True),list(range(9,9-len(alpha),-1)))
answer = 0
for i,j in temp : 
    answer += i*j
print(answer)
