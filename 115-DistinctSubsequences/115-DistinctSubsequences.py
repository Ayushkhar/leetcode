# Last updated: 6/6/2026, 10:26:48 PM
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #applying lcs in the leet
        dp={}
        l1=len(s)
        l2=len(t)
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            
            if s[i]==t[j]:
                dp[(i,j)]=solve(i+1,j+1)+solve(i+1,j)
            else:
                dp[(i,j)]=solve(i+1,j)

            return dp[(i,j)]
        return solve(0,0)

        # dp = [[0]*(l2+1) for _ in range(l1+1)]
        
        # for i in range(l1 + 1):
        #     dp[i][0] = 1
        # # for i in range(1,l1+1):
        # #     for j in range(1,l2+1):
        # #         if s[i-1]==t[j-1]:
        # #             dp[i][j]=1+dp[i-1][j-1]
        # #         else:
        # #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return dp
        
        
        