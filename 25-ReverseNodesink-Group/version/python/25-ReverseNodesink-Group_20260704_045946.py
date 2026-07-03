# Last updated: 7/4/2026, 4:59:46 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        curr = head
9        count = 0
10
11        while curr and count<k:
12            curr=curr.next
13            count+=1
14
15        if count<k:
16            return head
17
18        curr = head
19        prev = None 
20        for i in range(k):
21            temp = curr.next 
22            curr.next = prev 
23            prev = curr
24            curr= temp
25        
26        head.next = self.reverseKGroup(curr, k)
27        return prev 
28        