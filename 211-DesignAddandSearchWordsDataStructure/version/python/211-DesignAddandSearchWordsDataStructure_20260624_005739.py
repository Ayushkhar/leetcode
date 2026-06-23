# Last updated: 6/24/2026, 12:57:39 AM
1class WordDictionary:
2
3    def __init__(self):
4        self.children = [None] * 26
5        self.isleaf = False
6        
7
8    def addWord(self, word: str) -> None:
9        curr = self 
10        for i in word:
11            ind = ord(i) - ord('a')
12            if(curr.children[ind] is None):
13                curr.children[ind] = WordDictionary()
14            curr = curr.children[ind]
15        curr.isleaf= True
16
17    def search(self, word: str) -> bool:
18        def dfs(j,root):
19            curr = root
20            for i in range(j,len(word)):
21                ch = word[i]
22                if(ch == "."):
23                    for child in curr.children:
24                        if child and dfs(i+1,child):
25                            return True 
26                    return False 
27                ind = ord(ch) - ord('a')
28                if curr.children[ind] is None:
29                    return False
30
31                curr = curr.children[ind]
32            return curr.isleaf
33        return dfs(0,self)
34
35
36# Your WordDictionary object will be instantiated and called as such:
37# obj = WordDictionary()
38# obj.addWord(word)
39# param_2 = obj.search(word)