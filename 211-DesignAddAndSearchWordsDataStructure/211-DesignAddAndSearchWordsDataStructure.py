# Last updated: 6/28/2026, 12:42:20 PM
class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.isleaf = False 
        
    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            ind = ord(ch) - ord('a')
            if(curr.children[ind] is None):
                curr.children[ind] = WordDictionary()
            curr = curr.children[ind]
        curr.isleaf = True
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j,len(word)):
                ch = word[i]
                if(ch == "."):
                    for child in curr.children:
                        if(child and dfs(i+1, child)):
                            return True
                    return False
                        
                ind = ord(ch) - ord('a')
                if(curr.children[ind] is None):
                    return False 
                curr = curr.children[ind]
            return curr.isleaf 

        return dfs(0,self)
                
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)