# Last updated: 7/9/2026, 12:37:49 PM
1class TrieNode():
2    def __init__(self):
3        self.children = [None] * 26
4        self.word = None 
5class Solution:
6    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
7        root = TrieNode()
8        
9    
10        for word in words:
11            curr = root
12            for ch in word:
13                ind = ord(ch) - ord('a')
14                if curr.children[ind] is None:
15                    curr.children[ind] = TrieNode()
16                curr = curr.children[ind]
17            curr.word = word
18
19        rows = len(board)
20        cols = len(board[0])
21        res = []
22
23        def dfs(r,c,node):
24            if r<0 or c<0 or r>=rows or c>=cols:
25                return
26            
27            ch = board[r][c]
28            if(ch == "#"):
29                return
30
31            ind = ord(ch) - ord('a')
32            if node.children[ind] is None:
33                return 
34            node = node.children[ind]
35            if node.word:
36                res.append(node.word)
37                node.word = None 
38            board[r][c] = "#"
39            dfs(r + 1, c, node)
40            dfs(r - 1, c, node)
41            dfs(r, c + 1, node)
42            dfs(r, c - 1, node)
43
44            board[r][c] = ch
45        for r in range(rows):
46            for c in range(cols):
47                dfs(r,c,root)
48        return res
49
50
51    
52
53
54        