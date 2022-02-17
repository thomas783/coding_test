# 양궁대회

def solution(n, info) : 
    maxi = 0
    ans = []
    for bit in range(1<<11-1,-1,-1) : 
        cnt = n
        tmp = [0 for _ in range(11)]
        for i in range(len(info)) : 
            if bit & (1 << i) and cnt >= info[i] + 1: 
                tmp[i] = info[i]+1
                cnt -= (info[i] + 1)
            if cnt == 0 : 
                break
        total1 = 0
        total2 = 0
        for i in range(11) : 
            if info[i] < tmp[i] :
                total2 += 10-i
            elif info[i] > tmp[i] : 
                total1 += 10-i
            else : 
                if info[i] != 0 : 
                    total1 += i
        total = total2 - total1
        if maxi < total : 
            maxi = total
            ans = [tmp]
        elif maxi == total : 
            ans.append(tmp)
    if maxi == 0 : 
        return [-1]
    ans = sorted(ans,key=lambda x : (x[10],x[9],x[8],x[7],x[6],x[5],x[4],x[3],x[2],x[1],x[0]),reverse=True)[0]
    if sum(ans) != n : 
        ans[-1] += n-sum(ans)
    return ans

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info))