# Last updated: 6/6/2026, 10:26:20 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        dp = [1] * len(nums)

        dp[0] =nums[0]
        dp[1] = max(nums[0],nums[1])
        prof=0

        for i in range(2,len(nums)):
            prof = dp[i-2] + nums[i]
            skp=dp[i-1]
            dp[i] =max(prof,skp)

        return dp[-1]




        