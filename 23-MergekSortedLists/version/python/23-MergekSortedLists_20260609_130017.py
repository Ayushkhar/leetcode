# Last updated: 6/9/2026, 1:00:17 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        if not lists:
9            return None 
10
11        merged=lists[0]
12        for i in range(1,len(lists)):
13            merged=self.mergetwo(merged,lists[i])
14
15        return merged 
16
17    def mergetwo(self,l1,l2):
18        dummy=ListNode(0)
19        curr=dummy 
20        while l1 is not None and l2 is not None:
21            if l1.val < l2.val:
22                curr.next=l1
23                l1=l1.next
24            else:
25                curr.next =l2
26                l2=l2.next 
27            curr=curr.next 
28        if l1 is None:
29            curr.next=l2
30        else:
31            curr.next=l1
32
33        return dummy.next 
34