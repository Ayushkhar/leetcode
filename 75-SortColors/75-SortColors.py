# Last updated: 6/6/2026, 10:26:57 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        j = 0
        k = len(nums) - 1

        while(j <= k):
            if nums[j] == 1:
                j = j + 1
            elif nums[j] == 0:
                nums[j],nums[i] = nums[i],nums[j]
                i = i + 1
                j = j + 1
            else:
                nums[j],nums[k] = nums[k],nums[j]
                k = k - 1
        