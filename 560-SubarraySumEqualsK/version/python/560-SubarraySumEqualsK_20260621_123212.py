# Last updated: 6/21/2026, 12:32:12 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        # sum = 0
4        cnt = 0
5        prefix_sum = 0
6        prfix_sum_cnt  = {0:1}
7
8        for num in nums:
9            prefix_sum += num
10            if(prefix_sum - k) in prfix_sum_cnt:
11                cnt += prfix_sum_cnt[prefix_sum - k]
12            if(prefix_sum in prfix_sum_cnt):
13                prfix_sum_cnt[prefix_sum]+=1
14            else:
15                prfix_sum_cnt[prefix_sum] = 1
16        return cnt