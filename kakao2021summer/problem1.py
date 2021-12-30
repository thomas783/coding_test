# 카카오 상반기 인턴 코테 1번

def solution(s) :
    alpha = ['zero','one','two','three','four','five','six','seven','eight','nine']
    nums = [str(i) for i in list(range(10))]
    dic = dict()
    for i,j in enumerate(alpha) :
        dic[j] = i
    answer = ''
    temp = ''
    for i in s : 
        if i in nums : 
            answer += i # 숫자면 그대로 넣어줌
        else : 
            temp += i
            if temp in dic.keys() : 
                answer += str(dic[temp])
                temp = ''
    return int(answer)

solution("one4seveneight")