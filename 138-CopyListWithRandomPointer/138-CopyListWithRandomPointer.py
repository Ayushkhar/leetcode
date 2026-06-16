# Last updated: 6/16/2026, 9:28:32 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head

        old_tonew={}
        while curr:
            old_tonew[curr] =Node(curr.val)
            curr=curr.next
        curr=head 
        while curr:
            copynode=old_tonew[curr]
            copynode.next =old_tonew[curr.next] if curr.next else None 
            copynode.random=old_tonew[curr.random] if curr.random else None 
            curr=curr.next 

        return old_tonew[head] if head else None

        