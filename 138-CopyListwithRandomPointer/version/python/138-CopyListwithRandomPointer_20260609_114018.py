# Last updated: 6/9/2026, 11:40:18 AM
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
12        if head is None:
13            return None 
14        curr=head
15
16        old_tonew={}
17        while curr:
18            old_tonew[curr] =Node(curr.val)
19            curr=curr.next
20        curr=head 
21        while curr:
22            copynode=old_tonew[curr]
23            copynode.next =old_tonew[curr.next] if curr.next else None 
24            copynode.random=old_tonew[curr.random] if curr.random else None 
25            curr=curr.next 
26
27        return old_tonew[head] if head else None
28
29        