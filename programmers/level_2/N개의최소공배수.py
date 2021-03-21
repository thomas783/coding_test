# Programmers_level_2_N개의 최소공배수
def gcd(a,b) : # 최대공약수를 구하는 함수
    a,b = max(a,b), min(a,b)
    while b>0 : 
        a,b = b, a% b 
    return a
def solution(arr) : 
    answer = arr[0]
    for item in arr[1:] : 
        temp1 = answer
        temp2 = item
        temp3 = gcd(temp1,temp2)
        answer = temp1 * temp2 / temp3 
    return answer