# Last updated: 6/6/2026, 10:27:10 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        a=[]
        res=[]
        for word in strs:
            a="".join(sorted(word))
            if a in hashmap:
                hashmap[a]=hashmap[a]+[word]
            else:
                hashmap[a]=[word]
        
        return list(hashmap.values())
            

        # for i in range(len(strs)):
            

        # for i in range(len(a)):
        #     for j in range(len(a)):
        #         if a[i]==a[j]:
        #             res.append

        # return a 

        # for w in strs:
        #     k="".join(sorted(w))
        #     hashmap[k]=w
        # return hashmap 


        # return hashmap
        