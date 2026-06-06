# Last updated: 6/6/2026, 10:26:43 PM
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=re.sub(r'[^a-zA-Z0-9]', '', s)
        s=a.lower()
        return True if s==s[::-1] else False