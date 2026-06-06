# Last updated: 6/6/2026, 10:25:44 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        while(i<len(s) and j<len(t)):
            if(s[i]==t[j]):
                i=i+1
                j=j+1
            else:
                j=j+1
        if i==len(s):
            return True
        else:
            return False


        
        