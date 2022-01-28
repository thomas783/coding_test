# 레벨 햄버거

import sys

def get_ans(n,x) :
    if n == 0 :
        if x == 0 : 
            return 0
        elif x == 1 : 
            return 1
    elif x == 1 : 
        return 0
    # 그 전 레벨 햄버거 전까지 경우
    elif x <= 1 + h[n-1] : 
        return get_ans(n-1,x-1)
    # 그 전 레벨 햄버거 끝까지 + 패티
    elif x == 1 + h[n-1] + 1 : 
        return p[n-1] + 1
    # 그 전 레벨 두번째 햄버거 전까지
    elif x <= 1 + h[n-1] + 1 + h[n-1] : 
        return p[n-1] + 1 + get_ans(n-1,x-(1+h[n-1]+1))
    # 전부 다인 경우
    else : 
        return p[n-1] + 1 + p[n-1]


input = sys.stdin.readline
n,x = map(int,input().split())
# h는 레벨 n 햄버거의 전체 재료수
# p는 레벨 n 햄버거의 패티수
h = [1 for _ in range(n+1)]
p = [1 for _ in range(n+1)]
for i in range(1,n+1) : 
    h[i] = 1 + h[i-1] + 1 + h[i-1] + 1
    p[i] = p[i-1] + 1 + p[i-1]
print(get_ans(n,x))