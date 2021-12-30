# N-Queen

def dfs(n) : 
    if n == N : 
        global ans
        ans += 1
    else : 
        for i in range(N) : 
            if visited[i] : 
                continue
            table[n] = i
            if check(n) : 
                visited[i] = True
                dfs(n+1)
                visited[i] = False

def check(n) : 
    for i in range(n) :
        if table[n] == table[i] or n-i == abs(table[n] - table[i]) : 
            return False
    return True 

N = int(input())
ans = 0
table = [0 for _ in range(N)]
visited = [False for _ in range(N)]
dfs(0)
print(ans)