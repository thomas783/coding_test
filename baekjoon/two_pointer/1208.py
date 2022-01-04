# 부분수열의 합 2

import sys
input = sys.stdin.readline
n, s = map(int,input().split())
li = list(map(int,input().split()))
ans = 0
m = n // 2
n = n - m
# 이분 분할을 통해 전체 계산량을 절반으로 줄인다.
# 그렇지 않으면 2^40을 계산해야함. -> 2^20 + 2^20으로 줄임
left = [0 for _ in range(1<<n)]
right = [0 for _ in range(1<<m)]
# 비트마스킹을 통해 넣을지 말지를 정해서 그 합을 계산해 넣어준다.
for i in range(1<<n) : 
    for j in range(n) : 
        if i & (1<<j) : 
            left[i] += li[j]
for i in range(1<<m) : 
    for j in range(m) : 
        if i & (1<<j) : 
            right[i] += li[j+n]
left = sorted(left)
right = sorted(right,reverse = True)
# two pointer를 이용해 양쪽에서 하나씩 골라 합을 구해 s와 같은지 확인
left_end,right_end,left_idx,right_idx,ans = (1<<n),(1<<m),0,0,0
while left_idx < left_end and right_idx < right_end : 
    if left[left_idx] + right[right_idx] == s : 
        c1,c2 = 1,1
        left_idx += 1
        right_idx += 1
        while left_idx < left_end and left[left_idx] == left[left_idx-1] : 
            c1 += 1
            left_idx += 1
        while right_idx < right_end and right[right_idx] == right[right_idx-1] : 
            c2 += 1
            right_idx += 1
        ans += c1 * c2
    # 합이 s보다 작다면 오름차순 정렬인 left를 이동
    elif right[right_idx] + left[left_idx] < s : 
        left_idx += 1 
    # 합이 s보다 크다면 내림차순 정렬인 right를 이동
    else : 
        right_idx += 1
# s가 0이라면 공집합의 경우를 제외
if s == 0 : 
    ans -= 1
print(ans)