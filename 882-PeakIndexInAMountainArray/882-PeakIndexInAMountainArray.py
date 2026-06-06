# Last updated: 6/6/2026, 10:25:16 PM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        m=max(arr)
        return arr.index(m)
        # for i in range(len(arr)):
            

        