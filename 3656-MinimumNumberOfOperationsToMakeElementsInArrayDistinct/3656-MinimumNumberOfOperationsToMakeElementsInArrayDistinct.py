# Last updated: 6/6/2026, 10:24:08 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        
        while (len(set(nums)) < len(nums)):
            nums = nums[3:]
            count = count+1
        return count


            
        

        