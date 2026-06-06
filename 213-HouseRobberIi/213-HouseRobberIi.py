# Last updated: 6/6/2026, 10:26:15 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_dep(nums[1:]),self.rob_dep(nums[:-1]))
        
    def rob_dep(self,nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp=[0]*(len(nums))

        dp[len(nums)-1]=nums[-1]
        dp[len(nums)-2]=max(nums[-1],nums[-2])

        for i in range(len(nums)-3,-1,-1):
            rob=nums[i]+dp[i+2]
            skp=dp[i+1]
            dp[i]=max(rob,skp)

        return dp[0]
