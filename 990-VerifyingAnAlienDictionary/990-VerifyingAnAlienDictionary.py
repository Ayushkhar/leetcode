# Last updated: 6/6/2026, 10:25:09 PM
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap ={}

        for i in range(len(words)):
            for j in range(len(words[i])):
                ch = words[i][j]
                hashmap[ch] = order.index(ch)

        for k in range(len(words)-1):
            w1=words[k]
            w2=words[k+1]

            j=0
            while j<len(w1) and j<len(w2):
                a=hashmap[w1[j]]
                b=hashmap[w2[j]]

                if a>b:
                    return False
                elif a<b:
                    break
                j+=1
            if j ==len(w2) and len(w1)>len(w2):
                return False
        return True

            

   
        
                

        return hashmap

     

        