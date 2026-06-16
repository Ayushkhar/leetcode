# Last updated: 6/16/2026, 9:28:59 PM
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        currlen = 0
        maxlen = 0
        self.stack = [-1]
        for i in range(len(s)):
            if(s[i]=="("):
                self.stack.append(i)
            else:
                self.stack.pop()
                if len(self.stack)==0:
                    self.stack.append(i)
                else:
                    currlen = i-self.stack[-1]
                    maxlen = max(maxlen,currlen)
        return maxlen

        