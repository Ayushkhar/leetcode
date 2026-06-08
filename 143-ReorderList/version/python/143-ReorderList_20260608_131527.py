# Last updated: 6/8/2026, 1:15:27 PM
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
13
14        while c1:
15            cnt+=1
16            c1=c1.next
17        c2=head
18        for i in range(cnt//2):
19            c2=c2.next
20
21        c3=c2.next
22        c2.next=None 
23        prev =None
24
25        while c3:
26            temp = c3.next 
27            c3.next=prev
28            prev=c3
29            c3=temp
30        c4=head
31        while prev:
32            temp1=c4.next 
33            temp2=prev.next
34
35            c4.next=prev
36            prev.next=temp1
37
38            c4=temp1
39            prev =temp2
40
41        # print(cnt)
42