# Last updated: 6/25/2026, 6:23:14 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l = 0
4        r = 0
5        seen = set()
6        ans = 0
7        while(r < len(s)):
8            if(s[r] not in seen):
9                seen.add(s[r])
10                ans = max(ans, r-l+1)
11                r+=1
12            else:
13                seen.remove(s[l])
14                l+=1
15        return ans 
16
17        