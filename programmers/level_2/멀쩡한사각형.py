# programmers level2 - 멀쩡한 사각형

def solution(w, h) :
    import math
    g = math.gcd(w,h)
    return w*h - (w+h-g)