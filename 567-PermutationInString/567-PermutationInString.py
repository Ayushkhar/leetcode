# Last updated: 6/6/2026, 10:25:29 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        hashmap1=defaultdict(int)
        for i in range(len(s1)):
            hashmap1[s1[i]]+=1

        for j in range(len(s2)-len(s1)+1):
            hashmap2=defaultdict(int)
            sld=s2[j:j+len(s1)]
            for k in range(len(sld)):
                hashmap2[sld[k]]+=1
            
            if hashmap1==hashmap2:
                return True 
        return False 

        