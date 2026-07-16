# Last updated: 7/16/2026, 6:37:44 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hsh = defaultdict(int)

        for i in range(len(nums)):
            hsh[nums[i]] += 1

        for key, value in hsh.items():
            if value == 1:
                return key 
                