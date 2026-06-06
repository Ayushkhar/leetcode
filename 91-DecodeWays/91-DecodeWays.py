# Last updated: 6/6/2026, 10:26:55 PM
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] *(len(s)+1)
        onedig=0
        twodig=0
        dp[0]=1
        if s[0]=="0":
            dp[1]=0
        else:
            dp[1]=1

        for i in range(2,len(s)+1):
            res=0
            onedig = int(s[i-1:i])
            twodig = int(s[i-2:i])
            if 1<=onedig<=9:
                res=dp[i-1]
                dp[i]=res     
            if (10<=twodig<=26):
                res=res+dp[i-2]
                dp[i]=res    
        return dp[-1]
        