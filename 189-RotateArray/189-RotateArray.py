# Last updated: 6/6/2026, 10:26:21 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l1 = len(nums)
        k=k%l1
        l = len(nums) - k
        f = nums[l:]
        nums[:]=f + nums[:l]


    
     


        