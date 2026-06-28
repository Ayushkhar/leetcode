# Last updated: 6/28/2026, 6:09:55 AM
class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.word = None 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
    
        for word in words:
            curr = root
            for ch in word:
                ind = ord(ch) - ord('a')
                if curr.children[ind] is None:
                    curr.children[ind] = TrieNode()
                curr = curr.children[ind]
            curr.word = word

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r,c,node):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            
            ch = board[r][c]
            if(ch == "#"):
                return

            ind = ord(ch) - ord('a')
            if node.children[ind] is None:
                return 
            node = node.children[ind]
            if node.word:
                res.append(node.word)
                node.word = None 
            board[r][c] = "#"
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = ch
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return res


    


        