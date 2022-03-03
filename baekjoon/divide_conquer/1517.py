# 버블 소트

import sys

def merge_sort(start,end) : 
    global cnt
    if start < end : 
        mid = (start+end)//2
        merge_sort(start,mid)
        merge_sort(mid+1,end)
        a = start
        b = mid+1
        tmp = []
        while a <= mid and b <= end : 
            if li[a] <= li[b] : 
                tmp.append(li[a])
                a += 1
            else : 
                tmp.append(li[b])
                b += 1
                cnt += (mid-a+1)
        if a<= mid : 
            tmp += li[a:mid+1]
        if b <= end : 
            tmp += li[b:end+1]
        for i in range(len(tmp)) :
            li[start+i] = tmp[i]

n = int(input())
li = list(map(int,input().split()))
cnt = 0
merge_sort(0,n-1)
print(cnt)