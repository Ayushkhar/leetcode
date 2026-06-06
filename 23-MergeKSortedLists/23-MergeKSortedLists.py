# Last updated: 6/6/2026, 10:27:21 PM
from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minh = []
        
        # Push the head of each non-empty linked list into the heap
        for i in lists:
            if i:
                heappush(minh, (i.val, id(i), i))  # Add id(i) to break ties
        
        dup = ListNode(0)  
        current = dup
    
        while minh:
            _, _, node = heappop(minh)  
            current.next = node  
            current = current.next  
            
            if node.next:  
                heappush(minh, (node.next.val, id(node.next), node.next))  # Push next node
    
        return dup.next
