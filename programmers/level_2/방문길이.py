# Programmers_level_3_방문 길이

def move(curr,s) : 
    if s == 'U' and curr[3] != 5 : 
        curr = [curr[2],curr[3],curr[2],curr[3]+1]
    elif s == 'D' and curr[3] != -5 : 
        curr = [curr[2],curr[3],curr[2],curr[3]-1]
    elif s == 'R' and curr[2] != 5 : 
        curr = [curr[2],curr[3],curr[2] + 1,curr[3]]
    elif s == 'L' and curr[2] != -5: 
        curr = [curr[2],curr[3],curr[2] - 1,curr[3]]
    return curr

def solution(dirs) : 
    his = []
    dirs = [i for i in dirs]
    start = [0,0,0,0]
    answer = 0
    for i in range(len(dirs)) :
        temp = move(start,dirs[i])
        if temp not in his : 
            his.append(temp)
            his.append([temp[2],temp[3],temp[0],temp[1]])
            start = temp
            answer += 1
        else : 
            start = temp
    return answer