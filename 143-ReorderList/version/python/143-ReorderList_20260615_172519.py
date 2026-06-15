# Last updated: 6/15/2026, 5:25:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        cnt = 0
12        curr=head
13        while curr!=None:
14            cnt+=1
15            curr=curr.next 
16        c1=head
17        for i in range(cnt//2):
18            c1=c1.next
19        curr =c1.next 
20        c1.next=None 
21        prev =None 
22        while curr:
23            temp1 =curr.next 
24            curr.next=prev 
25            prev = curr
26            curr=temp1
27        c3=head 
28        while prev:
29            t1=c3.next 
30            t2=prev.next
31
32            c3.next=prev 
33            prev.next=t1
34
35            c3=t1
36            prev =t2
37        # return head
38
39
40        