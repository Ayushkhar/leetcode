# Last updated: 6/6/2026, 10:26:09 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prfx=[1]*len(nums)
        suffx=[1]*len(nums)
        res=[]
        for i in range(1,len(nums)):
            prfx[i]=prfx[i-1] *nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffx[j]=suffx[j+1]*nums[j+1]

        for k in range(len(nums)):
            res.append(prfx[k]*suffx[k])

        return res