# Last updated: 6/6/2026, 10:25:59 PM
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
