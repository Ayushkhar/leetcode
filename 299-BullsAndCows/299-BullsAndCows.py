# Last updated: 6/6/2026, 10:25:58 PM
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        s = []
        g = []
        be = [0] * len(secret)
        ge = [0] * len(secret)

        for i in range(len(secret)):
            s.append(secret[i])
        for j in range(len(guess)):
            g.append(guess[j])

        for k in range(len(s)):
            if s[k] == g[k]:
                bull+=1
                be[k]=1
                ge[k]=1
        for i in range(len(s)):
            if be[i] == 1:
                continue
            for j in range(len(s)):
                if ge[j] == 0 and s[i] == g[j]:
                    cow+=1
                    ge[j] = 1
                    break
        return str(bull) + 'A' + str(cow) + 'B'

        
   
                

