# Last updated: 6/9/2026, 1:39:29 PM
1class Solution:
2    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
3        if not lists:
4            return None  
5        merged =lists[0]
6        for i in range(1,len(lists)):
7            merged=self.mergetwolist(merged,lists[i])
8
9        return merged 
10
11    def mergetwolist(self,l1,l2):
12        dummy =ListNode(0)
13        curr=dummy
14
15        while l1 is not None and l2 is not None:
16            if l1.val <l2.val:
17                curr.next=l1
18                l1=l1.next
19            else:
20                curr.next= l2
21                l2=l2.next 
22
23            curr=curr.next 
24
25        if l1 is None:
26            curr.next =l2
27        if l2 is None:
28            curr.next=l1
29
30        return dummy.next