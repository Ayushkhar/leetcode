# Last updated: 6/6/2026, 10:27:15 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        ind=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                k=nums[i-1]
                ind=i-1
                break 

        else:
            nums.reverse()
            return 

        for j in range(len(nums)-1,ind,-1):
            if nums[j]>k:
                temp=nums[j]
                nums[j]=nums[ind]
                nums[ind]=temp
                break 
        nums[ind+1:]=reversed(nums[ind+1:])
            
        