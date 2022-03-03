# 별 찍기 - 11

def recursive(n) : 
    global ans
    if n == 3 : 
        for s in ans : 
            print(''.join(s))
        return
    tmp = []
    for i in range(len(ans)) : 
        tmp.append([' ']*len(ans)+ans[i]+[' ']*len(ans))
    for i in range(len(ans)) : 
        tmp.append(ans[i]+[' ']+ans[i])
    ans = tmp
    recursive(n//2)

n = int(input())
ans = [[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]
recursive(n)