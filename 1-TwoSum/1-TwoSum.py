# Last updated: 6/6/2026, 10:27:34 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        arr=[]
        for i in range(len(nums)):
            sb=target -nums[i]
            if sb in hashmap:
                arr.append(i)
                a=hashmap[sb]
                arr.append(a)
            hashmap[nums[i]]=i
        return arr

        