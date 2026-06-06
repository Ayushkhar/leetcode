# Last updated: 6/6/2026, 10:26:12 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                a=hashmap[nums[i]]
                jh=abs(i-a)
                if jh<=k:
                    return True 
                    break
                
            hashmap[nums[i]]=i
        return False
        