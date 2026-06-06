# Last updated: 6/6/2026, 10:24:07 PM
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * n
        for query in queries:
            start = query[0]
            end = query[1]
            x = 1

            diff[start] += x
            if end + 1 < n:
                diff[end + 1] -= x
        result = [0] * n
        cumSum = 0
        for i in range(n):
            cumSum += diff[i]
            result[i] = cumSum
        for i in range(n):
            if result[i] < nums[i]:
                return False

        return True
