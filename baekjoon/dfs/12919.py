# A와 B 2

import sys

def dfs(end) : 
    if len(end) == len(start) : 
        if end == start : 
            print(1)
            sys.exit(0)
        return
    if end[0] == 'B' : 
        end = end[::-1][:-1]
        dfs(end)
        end = (end+['B'])[::-1]
    if end[-1] == 'A' :
        end = end[:-1]
        dfs(end)
        end = end + ['A']

input = sys.stdin.readline
start = list(map(str,input().rstrip()))
end = list(map(str,input().rstrip()))
dfs(end)
print(0)