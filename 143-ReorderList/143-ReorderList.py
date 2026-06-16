# Last updated: 6/16/2026, 9:28:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cnt = 0
        curr=head
        while curr!=None:
            cnt+=1
            curr=curr.next 
        c1=head
        for i in range(cnt//2):
            c1=c1.next
        curr =c1.next 
        c1.next=None 
        prev =None 
        while curr:
            temp1 =curr.next 
            curr.next=prev 
            prev = curr
            curr=temp1
        c3=head 
        while prev:
            t1=c3.next 
            t2=prev.next

            c3.next=prev 
            prev.next=t1

            c3=t1
            prev =t2
        # return head


        