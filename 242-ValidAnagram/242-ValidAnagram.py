# Last updated: 6/6/2026, 10:26:05 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1=defaultdict(int) 
        hashmap2=defaultdict(int) 
    
        for i in range(len(s)):
            hashmap1[s[i]]+=1
        for j in range(len(t)):
            hashmap2[t[j]]+=1
        return hashmap2==hashmap1


        