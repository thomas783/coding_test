# 로또

from itertools import combinations
temp = list(map(int,input().split()))
while True : 
    k,S = temp[0], temp[1:]
    for i in combinations(S,6) : 
        print(' '.join([str(j) for j in i]))    
    temp = list(map(int,input().split()))
    if temp == [0] : 
        break
    else : 
        print('')