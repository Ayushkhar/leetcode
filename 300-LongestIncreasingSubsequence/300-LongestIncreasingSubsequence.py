# Last updated: 6/6/2026, 10:25:56 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*(len(nums))
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        