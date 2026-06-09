# Last updated: 6/9/2026, 12:15:11 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        result = []
9        # current = head
10
11        for head in lists:
12            curr=head
13            while curr:
14                result.append(curr.val)
15                curr=curr.next 
16
17        result.sort()
18        dummy=ListNode(0)
19        temp =dummy
20
21        for val in result:
22            temp.next=ListNode(val)
23            temp=temp.next 
24
25        return dummy.next 
26        
27        
28    
29        