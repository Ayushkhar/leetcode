# Last updated: 6/6/2026, 10:26:16 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        min_lenw=float('inf')
        curr_sum=0
        for right in range(len(nums)):
            curr_sum=curr_sum+nums[right]
            while curr_sum>=target:
                min_window=right-left+1
                min_lenw=min(min_lenw,min_window)
                curr_sum=curr_sum-nums[left]
                left=left+1
        return 0 if min_lenw==float('inf') else min_lenw

        