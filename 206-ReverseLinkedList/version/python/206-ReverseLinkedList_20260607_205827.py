# Last updated: 6/7/2026, 8:58:27 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        curr = head
9        prev =None
10
11        while curr:
12            temp =curr.next
13            curr.next=prev
14            prev =curr
15            curr=temp
16
17        return prev
18
19        