# Last updated: 6/6/2026, 10:24:11 PM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):

            x=nums.index(min(nums))
            
            nums[x]=nums[x] * multiplier
        return nums