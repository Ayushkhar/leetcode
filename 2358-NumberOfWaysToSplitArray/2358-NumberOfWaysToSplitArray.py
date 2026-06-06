# Last updated: 6/6/2026, 10:24:29 PM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        Sum=sum(nums)
        acc, cnt=0, 0
        for i in range(n-1):
            acc+=nums[i]
            cnt+=(2*acc>=Sum)
        return cnt
        
        