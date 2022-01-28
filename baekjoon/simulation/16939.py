# 2x2x2 큐브

import sys

def check(li) : 
    for i in range(0,24,4) : 
        if not (li[i] == li[i+1] == li[i+2] == li[i+3]) : 
            return False
    return True

# 맨 밑바닥을 기준으로 왼쪽으로 돌리기
def tilt_left(li) : 
    li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9],li[13],li[15],li[16],li[18]\
        = li[16],li[18],li[5],li[7],li[4],li[6],li[13],li[15],li[3],li[2],li[9],li[8]
    return li

def is_ans(li) : 
    tilt_left(li)
    if check(li) : 
        print(1)
        sys.exit(0)
    tilt_left(li)
    tilt_left(li)
    if check(li) : 
        print(1)
        sys.exit(0)
    tilt_left(li)

input = sys.stdin.readline
li = list(map(int,input().split()))
# 총 90도로 왼쪽 혹은 오른쪽 두가지, 면은 6개 총 12가지 가능
is_ans(li)
# 밑 바닥이 1,2,3,4인 경우
tmp = [li[23]]+[li[22]]+[li[21]]+[li[20]] + li[0:8] + [li[14]] + [li[12]] + [li[15]] + [li[13]]\
    + [li[17]] + [li[19]] + [li[16]] + [li[18]] +[li[11]]+[li[10]]+[li[9]]+[li[8]]
is_ans(tmp)
# 밑 바닥이 9,10,11,12인 경우
tmp = li[4:12] + [li[23]]+[li[22]]+[li[21]]+[li[20]] + [li[13]]+[li[15]]+[li[12]]+[li[14]]\
    + [li[18]]+[li[16]]+[li[19]]+[li[17]] +[li[11]]+[li[10]]+[li[9]]+[li[8]]
is_ans(tmp)
# 밑 바닥이 13,14,15,16인 경우
tmp = [li[1]]+[li[3]]+[li[0]]+[li[2]] + li[12:16] + [li[10]]+[li[8]]+[li[11]]+[li[9]]\
    + li[20:24] + li[4:8] + li[16:20]
is_ans(tmp)
# 밑 바닥이 17,18,19,20인 경우
tmp = [li[2]]+[li[0]]+[li[3]]+[li[1]] + li[16:20] + [li[9]]+[li[11]]+[li[8]]+[li[10]]\
    + li[4:8] + li[20:24] + li[12:16]
is_ans(tmp)
# 밑 바닥이 21,22,23,24인 경우
tmp = [li[3]]+[li[2]]+[li[1]]+[li[0]] + li[20:24] + [li[11]]+[li[10]]+[li[9]]+[li[8]]\
    + li[16:20] + li[12:16] + li[4:8]
is_ans(tmp)
print(0)