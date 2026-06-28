# Last updated: 6/28/2026, 6:09:32 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum = 0
        cnt = 0
        prefix_sum = 0
        prfix_sum_cnt  = {0:1}

        for num in nums:
            prefix_sum += num
            if(prefix_sum - k) in prfix_sum_cnt:
                cnt += prfix_sum_cnt[prefix_sum - k]
            if(prefix_sum in prfix_sum_cnt):
                prfix_sum_cnt[prefix_sum]+=1
            else:
                prfix_sum_cnt[prefix_sum] = 1
        return cnt