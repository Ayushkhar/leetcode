# Last updated: 6/6/2026, 10:25:25 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt=0 

        for i in range(len(s)):
            # For odd length  
            l=i
            r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                cnt+=1

            # For even length 
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                cnt+=1

        return cnt 
        
        