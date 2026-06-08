# Last updated: 6/8/2026, 9:00:25 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy =ListNode(0)
9        dummy.next=head 
10        slow=fast=dummy 
11
12
13        for _ in range(n):
14            fast=fast.next
15
16        while fast.next!=None:
17            slow=slow.next
18            fast =fast.next 
19
20        slow.next=slow.next.next 
21        return dummy.next 
22