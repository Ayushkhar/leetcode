# Last updated: 6/6/2026, 10:25:54 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = amount+1
        dp = [inf] *(amount+1)
        dp[0] = 0
        prev = [-1] * (amount+1)


        for x in range(1,amount+1):
            for c in coins:
                if x-c>=0 and dp[x-c]+1<dp[x]:
                    dp[x] = dp[x-c] +1
                    prev[x] = c

        if dp[amount] >= inf:
            return -1
        
        return dp[-1]




        