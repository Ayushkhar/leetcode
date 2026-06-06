# Last updated: 6/6/2026, 10:26:25 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #By using hashmap
        hashs={}
        for i in range(len(nums)):
            if nums[i] in hashs:
                hashs[nums[i]]+=1
            else:
                hashs[nums[i]]=1
        return max(hashs,key=hashs.get)
        