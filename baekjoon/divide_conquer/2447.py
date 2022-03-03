# 별 찍기 - 10

def recursive(n) : 
    global ans
    if n // 3 == 1 : 
        for s in ans : 
            print(''.join(s))
        return
    tmp = []
    for i in range(len(ans)) : 
        tmp.append(ans[i]*3)
    for i in range(len(ans)) : 
        tmp.append(ans[i]+[' ']*len(ans)+ans[i])
    for i in range(len(ans)) : 
        tmp.append(ans[i]*3)
    ans = tmp
    recursive(n//3)

n = int(input())
ans = [['*','*','*'],['*',' ','*'],['*','*','*']]
recursive(n)