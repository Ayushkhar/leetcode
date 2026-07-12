# Last updated: 7/13/2026, 1:26:43 AM
1class WordDictionary:
2
3    def __init__(self):
4        self.children = [None] * 26
5        self.isleaf =  False 
6    def addWord(self, word: str) -> None:
7        curr = self
8        for ch in word:
9            index = ord(ch) - ord('a')
10            if curr.children[index] is None:
11                curr.children[index] = WordDictionary()
12            curr = curr.children[index]
13            
14        curr.isleaf = True 
15    
16    def search(self, word: str) -> bool:
17        def dfs(i, curr):
18            if i == len(word):
19                return curr.isleaf 
20            ch = word[i]
21
22            if ch == ".":
23                for child in curr.children:
24                    if child is not None:
25                        if dfs(i + 1, child):
26                            return True 
27                return False 
28
29            index = ord(ch) - ord('a')
30            if curr.children[index] is None:
31                return False 
32            return dfs(i + 1, curr.children[index])
33        return dfs(0, self)
34        
35
36
37# Your WordDictionary object will be instantiated and called as such:
38# obj = WordDictionary()
39# obj.addWord(word)
40# param_2 = obj.search(word)