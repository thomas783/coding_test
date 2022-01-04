# 두 배열의 합

import sys
input = sys.stdin.readline
s = int(input())
n = int(input())
li1 = list(map(int,input().split()))
m = int(input())
li2 = list(map(int,input().split()))
ans = 0
left = []
right = []
for i in range(n) : 
    for j in range(i+1,n+1) : 
        left.append(sum(li1[i:j]))
for i in range(m) : 
    for j in range(i+1,m+1) : 
        right.append(sum(li2[i:j]))
left = sorted(left)
right = sorted(right,reverse = True)
left_end,right_end,left_idx,right_idx = len(left),len(right),0,0
while left_idx < left_end and right_idx < right_end : 
    if left[left_idx] + right[right_idx] == s : 
        c1,c2 = 1,1
        left_idx += 1
        right_idx += 1
        while left_idx < left_end and left[left_idx] == left[left_idx-1] : 
            c1 += 1
            left_idx +=1
        while right_idx < right_end and right[right_idx] == right[right_idx-1] : 
            c2 += 1
            right_idx += 1
        ans += c1 * c2
    elif left[left_idx] + right[right_idx] < s : 
        left_idx += 1
    else : 
        right_idx += 1
print(ans)
