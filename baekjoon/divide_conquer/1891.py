# 사분면

import sys

def find_loc(num,idx,r,c,size) :
    global num_r,num_c
    if size == 0 : 
        num_r,num_c = r,c
        return
    if num[idx] == "1" :
        find_loc(num,idx+1,r,c+size,size//2)
    elif num[idx] == "2" :
        find_loc(num,idx+1,r,c,size//2)
    elif num[idx] == "3" :
        find_loc(num,idx+1,r+size,c,size//2)
    else : 
        find_loc(num,idx+1,r+size,c+size,size//2)

def find_ans(num_r,num_c,size,ans) :
    if size == 0 :
        print(ans)
        return
    if 0 <= num_r < size and size <= num_c < size*2 : 
        find_ans(num_r,num_c-size,size//2,ans+'1')
    elif 0<= num_r < size and 0<= num_c < size : 
        find_ans(num_r,num_c,size//2,ans+'2')
    elif 0<= num_r < size*2 and 0<= num_c < size : 
        find_ans(num_r-size,num_c,size//2,ans+'3')
    elif 0<= num_r < size*2 and 0<= num_c < size*2 : 
        find_ans(num_r-size,num_c-size,size//2,ans+'4')

input = sys.stdin.readline
d,num = map(str,input().split())
d = int(d)
x,y = map(int,input().split())
num_r,num_c = 0,0
find_loc(num,0,num_r,num_c,(2**d)//2)
num_r -= y
num_c += x
if 0<= num_r < 2**d and 0<= num_c < 2**d : 
    find_ans(num_r,num_c,(2**d)//2,'')
else : 
    print(-1)