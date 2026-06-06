# Last updated: 6/6/2026, 10:25:19 PM
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = [root.val]  # Visit root
        for child in root.children:
            result.extend(self.preorder(child))  
        
        return result


        