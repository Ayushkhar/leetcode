# Last updated: 6/6/2026, 10:27:18 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k=k+1

        nums=nums[:k]
        return k
        