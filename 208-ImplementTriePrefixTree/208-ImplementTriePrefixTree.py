# Last updated: 6/28/2026, 12:42:21 PM
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isleaf = False
    def insert(self, word: str) -> None:
        curr = self
        for k in word:
            ind = ord(k) - ord('a')
            if(curr.children[ind] is None):
                curr.children[ind] = Trie()
            curr= curr.children[ind]
        curr.isleaf = True

    def search(self, word: str) -> bool:
        curr = self 
        for k in word:
            ind = ord(k) - ord('a')
            if(curr.children[ind] is None):
                return False 
            curr = curr.children[ind]
        return curr.isleaf

    def startsWith(self, prefix: str) -> bool:
        curr = self 
        for ch in prefix:
            ind = ord(ch) - ord('a')
            if(curr.children[ind] is None):
                return False
            curr= curr.children[ind]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)