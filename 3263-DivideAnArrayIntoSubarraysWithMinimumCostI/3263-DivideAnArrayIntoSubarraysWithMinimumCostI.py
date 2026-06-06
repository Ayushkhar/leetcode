# Last updated: 6/6/2026, 10:24:16 PM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        firstmin=float('inf')
        secmin=float('inf')

        for i in range(1,len(nums)):
            if nums[i] < firstmin:
                secmin=firstmin
                firstmin=nums[i]
            elif nums[i] < secmin:
                secmin=nums[i]
        return nums[0] + firstmin +secmin