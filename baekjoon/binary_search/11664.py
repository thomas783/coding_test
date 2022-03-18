# 선분과 점

x1,y1,z1,x2,y2,z2,x3,y3,z3 = map(int,input().split())
ans = float('inf')
while True : 
    mx,my,mz = (x1+x2)/2,(y1+y2)/2,(z1+z2)/2
    left = ((x1-x3)**2+(y1-y3)**2+(z1-z3)**2)**0.5
    mid = ((mx-x3)**2+(my-y3)**2+(mz-z3)**2)**0.5
    right = ((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)**0.5
    if abs(ans-mid) <= 1e-6:
        print('%0.10f'%ans)
        exit()
    if mid < ans : 
        ans = mid
    if left > right : 
        x1,y1,z1 = mx,my,mz
    else : 
        x2,y2,z2 = mx,my,mz