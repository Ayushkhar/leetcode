# Last updated: 6/8/2026, 8:38:04 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        slow=head
9        fast =head
10        curr=head 
11
12        for _ in range(n):
13            fast=fast.next
14        
15        while fast==None:
16            return slow.next 
17
18        while fast.next!=None:
19            slow=slow.next 
20            fast=fast.next 
21        # slow.next.next=None
22        slow.next=slow.next.next
23        return head
24
25       
26
27        
28        