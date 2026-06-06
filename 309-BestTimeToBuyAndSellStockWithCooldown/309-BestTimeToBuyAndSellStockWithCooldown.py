# Last updated: 6/6/2026, 10:25:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy=True
        dp={}
        result=self.solve(prices,0,n,buy,dp)
        
        return result
        
    def solve(self,prices,day,n,buy,dp):
        if day>=n:
            return 0
        profit=0

        if (day,buy) in dp:
            return dp[(day,buy)]
        if buy:
            # Selling prc-buyingprc
            take= self.solve(prices,day+1,n,False,dp) -prices[day]
            not_take=self.solve(prices,day+1,n,True,dp)
            dp[(day,buy)]= max(take,not_take)
        else:
            sell=self.solve(prices,day+2,n,True,dp)+prices[day]
            not_sell=self.solve(prices,day+1,n,False,dp)
            dp[(day,buy)]= max(sell,not_sell)

        return dp[(day,buy)]

        