# Last updated: 6/6/2026, 10:26:35 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp= [0] *(len(s)+1)

        dp[0]=1
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i]=1
                    break
                
        return True if dp[-1]==1 else False

        