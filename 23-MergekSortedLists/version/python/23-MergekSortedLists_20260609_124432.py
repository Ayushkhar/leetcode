# Last updated: 6/9/2026, 12:44:32 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        res=[]
9        for head in lists:
10            curr=head
11            while curr:
12                res.append(curr.val)
13                curr=curr.next
14
15        res.sort()
16
17        dummy=ListNode(0)
18        temp =dummy
19        for val in res:
20            temp.next=ListNode(val)
21            temp=temp.next 
22
23        return dummy.next 
24
25         
26        