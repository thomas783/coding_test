# 숫자 카드

import sys
def merge_sort(unsorted_list) : 
    if len(unsorted_list) <= 1 : 
        return unsorted_list
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1,right1)

def merge(left,right) : 
    i,j = 0,0
    sorted_list = []
    while (i<len(left)) and (j<len(right)) : 
        if left[i] < right[j] : 
            sorted_list.append(left[i])
            i+=1
        else : 
            sorted_list.append(right[j])
            j+=1
    while i<len(left) : 
        sorted_list.append(left[i])
        i+=1
    while j<len(right) : 
        sorted_list.append(right[j])
        j+=1
    return sorted_list


input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
m = int(input())
ms = list(map(int,input().split()))
# nlogn
li = merge_sort(li)
ans = []
for i in ms : 
    left = 0
    right = len(li)-1
    flag = False
    while left <= right : 
        mid = (left+right)//2
        if li[mid] > i : 
            right = mid-1
        elif li[mid] == i : 
            ans.append('1')
            flag = True
            break
        else : 
            left = mid+1
    if not flag : 
        ans.append('0')
print(' '.join(ans))