# Last updated: 7/9/2026, 12:39:11 PM
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum =float('-inf')
        currmax = 0

        minsum = float('inf')
        currmin = 0
        total =sum(nums)
    
        for i in range(len(nums)):
            currmax = max(nums[i],nums[i] + currmax)
            maxsum = max(maxsum, currmax)

            currmin = min(nums[i], nums[i] + currmin)
            minsum = min(minsum, currmin) 
        if maxsum < 0:
            return maxsum
        return max(maxsum, total-minsum)
      
       

        