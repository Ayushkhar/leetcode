# Last updated: 6/6/2026, 10:27:07 PM
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canjump = 0
        if len(nums)>=2:
            flag = len(nums) - 1 
            i = len(nums) - 2
            while i >= 0:
                if flag - i <= nums[i]:  
                    flag = i
                    canjump = 1
                else:
                    canjump = 0 
                i=i-1
  
            if canjump == 1:
                return True
            else:
                return False
        else:
            return True
