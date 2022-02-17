# 주차 요금 계산

def solution(fees, records) : 
    dic = dict()
    parked = dict()
    for i in records : 
        t,num,b = i.split()
        if b == 'IN' : 
            parked[num] = int(t[:2]) * 60 + int(t[3:])
        else : 
            if num in dic : 
                dic[num]+= int(t[:2]) * 60 + int(t[3:]) - parked[num]
            else : 
                dic[num] = int(t[:2]) * 60 + int(t[3:]) - parked[num]
            del parked[num]
    for num,t in parked.items() : 
        if num in dic : 
            dic[num]+= (23*60+59-t)
        else : 
            dic[num] = 23*60+59-t
    ans = dict()
    for num, t in dic.items() : 
        total = fees[1]
        if t > fees[0] : 
            t -= fees[0]
            if t % fees[2] == 0 : 
                total += t // fees[2] * fees[3]
            else : 
                total += (t // fees[2] + 1) * fees[3]
        ans[num] = total
    ans = [t for num,t in sorted(ans.items(),key=lambda x : x[0])]
    return ans
fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees,records))