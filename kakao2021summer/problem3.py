# 카카오 상반기 인턴 코테 3번

from collections import deque

def solution(n, k, cmd) :
    answer = list('O' * n)
    curr = 0
    q = deque()
    for i in range(n) : 
        q.append(str(i))
    q.reverse()
    q.rotate(k)
    deleted = deque()
    for c in cmd : 
        if c[0] == 'D' : 
            n = int(c[2:])
            q.rotate(n)
        elif c[0] == 'U' : 
            n = int(c[2:])
            q.rotate(-n)
        elif c[0] == 'C' : 
            temp = q.pop()
            temp2 = q.pop()
            if int(temp) > int(temp2) : # 마지막을 삭제하는 경우
                q.append(temp2)
                last = q.popleft()
                q.append(last)
                deleted.append(temp)
            else : 
                q.append(temp2)
                deleted.append(temp)
            answer[int(temp)] = 'X'
        elif c[0] == 'Z' :
            temp = deleted.pop()
            flag = True
            for i in range(len(q)-1) : 
                a,b = int(q[i]),int(q[i+1])
                if a > int(temp) > b : 
                    q.insert(i,temp)
                    flag = False
                    break
                elif a > int(temp) and b > int(temp) : 
                    q.insert(i,temp)
                    flag = False
                    break
            if flag :
                q.insert(0,temp)
            answer[int(temp)] = 'O'
    return ''.join(answer)

n = 8
k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C",'Z','Z']
# cmd = ['C','U 5','C','D 5','Z','Z']
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# cmd = ['C','C','Z','Z']
print(solution(n,k,cmd))