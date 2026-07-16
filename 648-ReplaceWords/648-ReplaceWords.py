# Last updated: 7/16/2026, 6:36:44 PM
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isleaf = False 
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sen = sentence.split()
        root = Trie()
        # Construction
        for word in dictionary:
            curr = root
            for ch in word:
                index = ord(ch) - ord('a')
                if curr.children[index] is None:
                    curr.children[index] = Trie()
                curr = curr.children[index]
            curr.isleaf = True 
        # Logic
        res = []
        for w in sen:
            curr = root
            prefix = ""
            replace = False
            for ch_s in w:
                index= ord(ch_s) - ord('a')
                if curr.children[index] is None:
                    res.append(w)
                    replace = True
                    break
                curr = curr.children[index]
                prefix+=ch_s
                if curr.isleaf:
                    replace = True
                    res.append(prefix)
                    break
            if replace is False:
                res.append(w)
          
        return " ".join(res)
                


        