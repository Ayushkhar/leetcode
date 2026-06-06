# Last updated: 6/6/2026, 10:26:44 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=[]
        for i in range(1,len(prices)):
            if(prices[i-1]<prices[i]):
                res=prices[i]-prices[i-1]
                l.append(res)
        return sum(l)
        

        