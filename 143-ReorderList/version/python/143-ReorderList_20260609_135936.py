# Last updated: 6/9/2026, 1:59:36 PM
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
11        curr=head 
12        cnt=0
13        while curr:
14            cnt+=1
15            curr=curr.next 
16        c2=head
17        for i in range((cnt//2)):
18            c2=c2.next
19        
20        curr=c2.next
21        c2.next =None 
22        prev =None 
23        while curr:
24            temp=curr.next
25            curr.next=prev
26            prev =curr
27            curr=temp
28        
29        c3=head
30        while prev:
31            temp1=c3.next 
32            temp2=prev.next 
33
34            c3.next=prev
35            prev.next=temp1
36
37            c3=temp1
38            prev=temp2 
39
40        
41
42
43
44
45            
46