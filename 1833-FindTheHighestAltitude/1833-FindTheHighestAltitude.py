# Last updated: 6/24/2026, 7:38:42 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        nums = [0] * (len(gain)+1)
        res =0 
        for i in range(1,len(nums)):
            res = res + gain[i-1]
            nums[i] = res

        return max(nums) 

            
        