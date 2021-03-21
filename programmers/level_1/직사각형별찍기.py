a, b = map(int, input().strip().split(' '))
answer = ''
for i in range(b-1) : 
    answer += '*'* a + '\n'
answer += '*'*a
print(answer)