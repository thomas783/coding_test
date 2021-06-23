n = input()
n = 'i' + n # 인덱스 맞추기 위해 넣은 것
dic = dict(zip(range(1,27),['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))
dp = [0 for _ in range(len(n))]
dp[0] = 1
dp[1] = 1
flag = True
if n[1] == '0' : 
    print(0)
else : 
    for i in range(2,len(n)) : 
        if n[i] == '0' : # 0인 경우 10,20만 가능하므로 예외처리
            if int(n[i-1] + n[i]) not in [10,20] : 
                dp[i] = 0
                flag = False
                break
            else : 
                dp[i] = dp[i-2]
        else : 
            dp[i] = dp[i-1] # 1~9인 경우 하나전 값 더해줌
            if int(n[i-1] + n[i]) in range(11,27) : # 11~27로 만들어줄 수 있는 경우 두개전 값 더해줌
                dp[i] += dp[i-2]
        dp[i] %= 1000000
    if flag : 
        print(dp[-1])
    else : 
        print(0)