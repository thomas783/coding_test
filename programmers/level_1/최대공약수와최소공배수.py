# programmers 최대공약수와 최소공배수
def solution(n, m) :
    answer = []
    for i in range(2,n+1)[::-1] :
        if (n % i == 0) and (m % i == 0):
            answer.append(i)
            break
    if answer == [] : 
        answer.append(1)
    for j in range(m,n*m+1) : 
        if (j % n == 0) and (j % m == 0) :
            answer.append(j)
            break
    return answer