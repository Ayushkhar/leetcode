# Last updated: 6/6/2026, 10:25:50 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1

        a= sorted(hashmap,key=hashmap.get)
       
        return a[len(a)-k:]
