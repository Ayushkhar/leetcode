# Last updated: 6/8/2026, 7:53:34 AM
1class Solution:
2    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
3
4        dummy =ListNode(-1)
5        curr =dummy
6        while list1 is not None and list2 is not None:
7            if list1.val < list2.val:
8                curr.next= list1
9                list1=list1.next
10            else:
11                curr.next= list2
12                list2=list2.next
13            curr=curr.next
14        if list1 is None:
15            curr.next=list2
16            # list2=list2.next
17        if list2 is None:
18            curr.next=list1
19            # list1=list1.next
20            
21        
22
23        return dummy.next
24
25
26
27
28
29        