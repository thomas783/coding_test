# Programmers_level_2_문자열 압축

def solution(s) : 
    answer = len(s)
    for i in range(1,len(s)+1) : 
        count = 0
        count_li = []
        start = i
        li = [s[:i]]
        end = 0
        while end < len(s) - 1 : 
            end = start + i
            if li[-1] == s[start:end] : 
                count += 1
            else : 
                li.append(s[start:end])
                if count != 0 : 
                    count_li.append(count)
                count = 0
            start = end
        if li[-1] == s[end:] : 
            count += 1
            count_li.append(count)
        else : 
            li.append(s[end:])
            if count != 0 : 
                count_li.append(count)
                count = 0
        count_li = ''.join([str(i+1) for i in count_li])
        answer = min(answer, len(count_li) + len(''.join(li)))
    return answer