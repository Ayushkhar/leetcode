# Last updated: 6/6/2026, 10:25:06 PM
class Solution:
    def fib(self, n: int) -> int:
        dp=[1]*(n+1)
        if n<=1:
            return n

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-2]
        