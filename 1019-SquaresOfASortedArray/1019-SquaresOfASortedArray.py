# Last updated: 6/6/2026, 10:25:05 PM
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)  
        k = []
        for i in range(0, len(nums)):
            res = nums[i] 
            m = res * res
            k.append(m)
        
        k = sorted(k) 
        return k

