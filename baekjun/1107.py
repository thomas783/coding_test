import sys
input = sys.stdin.readline
def check(num,broken_buttons) : # 하나씩 확인해보면서 하나라도 고장난 버튼을 누르면 넘어간다
    num = list(str(num))
    for i in num : 
        if int(i) in broken_buttons : 
            return False
    return True
n = int(input())
broken_n = int(input())
try : 
    broken_buttons = [i for i in map(int,input().split(' '))]
    answer = abs(100-n)
    for i in range(1000001) : # 
        if check(i,broken_buttons) : 
            answer = min(answer,len(str(i))+abs(n-i))
except : 
    if broken_n == 0 : 
        answer = min(len(str(n)),abs(100-n))
print(answer)