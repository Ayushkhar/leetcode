# Last updated: 6/15/2026, 4:37:04 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head is None or head.next is None:
9            return None
10        slow=head 
11        fast=head 
12
13        prev=None
14        
15        while fast and fast.next!=None:
16            prev =slow
17            slow=slow.next
18            fast =fast.next.next
19
20        prev.next=slow.next
21        return head
22            
23        temp=slow.next
24        temp.next=None
25        slow.next=None
26        slow.next=fast 
27        return head
28
29
30        