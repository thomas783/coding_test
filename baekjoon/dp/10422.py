# 괄호

# 괄호가 첫번째로 닫히는 인덱스를 j라 하고 전체 길이를 i이라 하면
# 결과적으로 i-j만큼으로 만들 수 있는 괄호문자열 * j길이로 만들수 있는
# 괄호 문자열을 모두 더하는 것과 같음.
import sys

t = int(input())
dp = [0 for _ in range(5001)]
dp[0] = 1
for i in range(2,5001,2) : 
    for j in range(2,i+1,2) : 
        dp[i] += (dp[j-2] * dp[i-j]) % 1000000007
for _ in range(t) : 
    n = int(input())
    print(dp[n] % 1000000007)