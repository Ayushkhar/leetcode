# Last updated: 6/6/2026, 10:24:56 PM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        st = 1
        cal = 0
        while True:
            cal = st
            cnt = 0
            for i in range(len(nums)):
                if cal + nums[i] >= 1:
                    cal = cal + nums[i]
                    cnt += 1
                else:
                    st += 1
                    break
            if cnt == len(nums):
                break
        return st