# 트리의 순회

import sys
sys.setrecursionlimit(10**9)

def preorder(in_l,in_r,post_l,post_r) : 
    if post_l <= post_r : 
        parents = postorder[post_r]
        print(parents,end=" ")
        p_idx = in_loc[parents]
        cnt_l = p_idx - in_l
        cnt_r = in_r - p_idx
        preorder(in_l,in_l+cnt_l-1,post_l,post_l+cnt_l-1)
        preorder(in_r-cnt_r+1,in_r,post_r-cnt_r,post_r-1)

input = sys.stdin.readline
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
in_loc = [0 for _ in range(n+1)]
for i in range(n) : 
    in_loc[inorder[i]] = i
preorder(0,n-1,0,n-1)