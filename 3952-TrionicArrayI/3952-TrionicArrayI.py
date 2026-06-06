# Last updated: 6/6/2026, 10:24:09 PM
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # Increasing wala case
        n=len(nums)
        i=0
        while(i+1<n and nums[i+1]>nums[i] ):
            i=i+1

        if(i == 0 or i == n-1):
            return False
        # decreasing wala case
        while(i+1<n and nums[i+1]<nums[i] ):
            i= i+1
        if(i==n-1):
            return False
        # Increasing wala case
        while(i+1<n and nums[i+1]>nums[i] ):
            i=i+1
        return i==n-1