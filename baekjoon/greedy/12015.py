# 가장 긴 증가하는 부분 수열 2

import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
ans = [0]
for i in li : 
    if ans[-1] < i : 
        ans.append(i)
    else : 
        left = 0
        right = len(ans)
        while left < right : 
            mid = (left+right) // 2
            if ans[mid]<i : 
                left = mid+1
            else : 
                right = mid
        ans[right] = i
print(len(ans)-1)