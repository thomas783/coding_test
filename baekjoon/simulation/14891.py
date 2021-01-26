# 톱니바퀴

import sys
def rotate(li, num) : 
    if num == 1 : # 시계방향 회전
        li = [li[-1]] + li[:-1]
    else : # 반시계방향 회전
        li = li[1:] + [li[0]]
    return li

gear = []
for _ in range(4) : 
    gear.append([int(i) for i in str(input())])
N = int(input())
can = list(range(4))
for _ in range(N) : 
    gear_num, dir = map(int,sys.stdin.readline().rstrip().split())
    gear_num -= 1
    gear[gear_num] = rotate(gear[gear_num],dir)
    left_past = gear_num
    left_next = gear_num - 1
    right_past = gear_num
    right_next = gear_num + 1
    left_dir = dir
    right_dir = dir
    while right_next in can : 
        if gear[right_past][2+right_dir] + gear[right_next][6] == 1 : # 시계방향으로 회전하면 비교대상이 하나 앞으로 넘어간다, 반시계면 하나 전으로 감
            right_dir = -right_dir
            gear[right_next] = rotate(gear[right_next],right_dir)
            right_past += 1
            right_next += 1
        else : 
            break
    while left_next in can : 
        if gear[left_past][6+left_dir] + gear[left_next][2] == 1 : 
            left_dir = -left_dir
            gear[left_next] = rotate(gear[left_next],left_dir)
            left_past -= 1
            left_next -= 1
        else : 
            break
answer = sum([gear[i][0] * 2**i for i in range(len(gear))])
print(answer)