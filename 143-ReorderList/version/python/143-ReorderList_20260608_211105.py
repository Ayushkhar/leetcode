# Last updated: 6/8/2026, 9:11:05 PM
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
11        c1=head
12        cnt =0
13        while c1:
14            cnt+=1
15            c1=c1.next
16        c2=head 
17        for i in range(cnt//2):
18            c2=c2.next
19        curr=c2.next 
20        c2.next=None
21        prev =None
22        while curr:
23            temp =curr.next
24            curr.next=prev
25            prev =curr
26            curr=temp
27        c3=head
28        while prev:
29            temp1=c3.next 
30            temp2=prev.next 
31
32            c3.next=prev
33            prev.next=temp1
34
35            c3=temp1
36            prev=temp2
37        
38
39        
40
41
42
43        