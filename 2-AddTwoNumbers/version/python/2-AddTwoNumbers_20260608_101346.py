# Last updated: 6/8/2026, 10:13:46 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy =ListNode(0)
9        curr=dummy
10        c=0
11
12        while l1 is not None or l2 is not None or c>0:
13            v1=l1.val if l1 is not None else 0
14            v2=l2.val if l2 is not None else 0
15
16            res=v1+v2+c
17            c=res//10
18            d=res%10
19
20            curr.next=ListNode(d)
21            
22            if l1 is not None:
23                l1=l1.next 
24            if l2 is not None:
25                l2=l2.next
26            curr=curr.next 
27        return dummy.next 
28            
29
30        