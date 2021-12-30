def solution(letters, k):
    if len(letters) == k : 
        return letters
    else : 
        stack = [letters[0]]
        for i in range(1,len(letters)) : 
            while letters[i] > stack[-1] and len(stack) + len(letters) - i > k : 
                stack.pop()
                if not stack :
                    break
            if len(stack) < k : 
                stack.append(letters[i])
        answer = ''.join(stack)
        return answer