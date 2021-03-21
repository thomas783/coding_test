# Programmers_level_2_올바른 괄호

def solution(s) : 
    if len(s) % 2 == 1 : 
        return False
    s = list(s)[::-1]
    stack = ''
    while s :
        stack += s.pop()
        if len(stack)>1 and stack[-2:] =='()' : 
            stack = stack[:-2]
    if len(stack) == 0 : 
        return True
    else : 
        return False