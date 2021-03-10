s1 = "ABCDGH"
s2 = "ACDGR"

n = len(s1)
m = len(s2)
dp = [[0 for x in range(m+1)]for y in range(n+1)]

maxlen = 0
for i in range(n+1):
    for j in range(m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        
        if dp[i][j] > maxlen:
            maxlen = dp[i][j]
print(maxlen)

