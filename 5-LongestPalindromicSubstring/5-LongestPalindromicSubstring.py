# Last updated: 6/6/2026, 10:27:30 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:

        res=[]

        for i in range(len(s)):
            l=i
            r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                res.append(s[l+1:r])
                
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                res.append(s[l+1:r])

        return max(res,key=len)
        