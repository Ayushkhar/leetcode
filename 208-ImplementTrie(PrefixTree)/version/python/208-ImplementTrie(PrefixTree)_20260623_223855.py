# Last updated: 6/23/2026, 10:38:55 PM
1class Trie:
2
3    def __init__(self):
4        self.children = [None] * 26
5        self.isleaf = False 
6    
7    def insert(self, word: str) -> None:
8        curr = self
9
10        for i in word:
11            ind = ord(i) - ord('a')
12            if(curr.children[ind] is None):
13                curr.children[ind] = Trie()
14
15            curr = curr.children[ind]
16        curr.isleaf = True
17
18    def search(self, word: str) -> bool:
19        curr = self
20        
21        for k in word:
22            ind = ord(k) - ord('a')
23            if(curr.children[ind] is None):
24                return False
25            curr = curr.children[ind]
26
27        return curr.isleaf
28
29    def startsWith(self, prefix: str) -> bool:
30        curr =  self
31        for k in prefix:
32            ind = ord(k) - ord('a')
33            if(curr.children[ind] is None):
34                return False 
35            else:
36                curr = curr.children[ind]
37
38        return True
39        
40
41
42# Your Trie object will be instantiated and called as such:
43# obj = Trie()
44# obj.insert(word)
45# param_2 = obj.search(word)
46# param_3 = obj.startsWith(prefix)