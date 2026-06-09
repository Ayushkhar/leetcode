# Last updated: 6/9/2026, 11:40:33 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        curr=head
13
14        old_tonew={}
15        while curr:
16            old_tonew[curr] =Node(curr.val)
17            curr=curr.next
18        curr=head 
19        while curr:
20            copynode=old_tonew[curr]
21            copynode.next =old_tonew[curr.next] if curr.next else None 
22            copynode.random=old_tonew[curr.random] if curr.random else None 
23            curr=curr.next 
24
25        return old_tonew[head] if head else None
26
27        