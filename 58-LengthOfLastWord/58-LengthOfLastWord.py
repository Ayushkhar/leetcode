# Last updated: 6/6/2026, 10:27:04 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spl=s.split()
        return len(spl[-1])
       