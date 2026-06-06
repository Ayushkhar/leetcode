# Last updated: 6/6/2026, 10:24:46 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        stack=[n-1]
        ans=[x for x in prices]
        for i in range(n-2, -1, -1):
            while stack and prices[i]<prices[stack[-1]]:
                stack.pop()
            if stack: ans[i]-=prices[stack[-1]]
            stack.append(i)
        return ans
        