# Last updated: 7/30/2026, 3:52:54 AM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        jmp = 0
4        farthest = 0
5        curr_ind = 0
6
7        for i in range(len(nums)-1):
8            farthest = max(farthest, i + nums[i])
9            if i == curr_ind:
10                jmp+=1
11                curr_ind = farthest
12
13        return jmp
14
15        