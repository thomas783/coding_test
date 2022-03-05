# 수 정렬하기 2

import sys

def merge_sort(li) :
    if len(li) <= 1 : 
        return li
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    i,j,k = 0,0,0
    while i < len(left) and j < len(right) : 
        if left[i] < right[j] : 
            li[k] = left[i]
            i += 1
        else : 
            li[k] = right[j]
            j += 1
        k += 1
    while i < len(left) :
        li[k] = left[i]
        i += 1
        k += 1
    while j < len(right) : 
        li[k] = right[j]
        j += 1
        k += 1
    return li

# 총 100만개까지 들어올 수 있기 때문에 O(nlogn)까지 가능
n = int(input())
li = []
for _ in range(n) : 
    li.append(int(input()))
ans = merge_sort(li)
for i in ans : 
    print(i)