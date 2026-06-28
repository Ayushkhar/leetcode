# Last updated: 6/28/2026, 12:41:12 PM
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0
        
        

        while(low <= high):
            mid = (low + high) // 2
            s = 0
            for j in range(len(piles)):
                s += math.ceil(piles[j] / mid)
        
            if(s<=h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        

        