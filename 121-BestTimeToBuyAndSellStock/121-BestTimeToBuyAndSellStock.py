# Last updated: 6/6/2026, 10:26:46 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minpr=float('inf')
        maxpr=0

        for i in prices:
            minpr= min(minpr,i)
            maxpr=max(maxpr,i-minpr)

        return maxpr

        