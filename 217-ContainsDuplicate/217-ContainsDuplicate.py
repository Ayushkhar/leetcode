# Last updated: 6/6/2026, 10:26:14 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        count=0
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
                break
            hashmap[nums[i]]=count+1
        return False
        
        