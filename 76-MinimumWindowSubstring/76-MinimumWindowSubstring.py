# Last updated: 6/28/2026, 6:10:49 AM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hsh1 = defaultdict(int)

        for i in range(len(t)):
            hsh1[t[i]] +=1
        
        hsh2 = defaultdict(int)
        have = 0
        need = len(hsh1)
        minl = float('inf')
        rng = [-1,-1]
        n = 0

        for j in range(len(s)):
            hsh2[s[j]]+=1


            if(s[j] in hsh2 and hsh1[s[j]] == hsh2[s[j]]):
                have += 1

            while(have == need):
                if((j - n + 1) < minl):
                    minl = j - n + 1
                    rng = [n, j]
                    
                hsh2[s[n]]-=1
                if(s[n] in hsh1 and hsh2[s[n]] < hsh1[s[n]]):
                    have -= 1
                n+=1
        n, j = rng
        return s[n:j+1] if minl != float('inf') else ""



