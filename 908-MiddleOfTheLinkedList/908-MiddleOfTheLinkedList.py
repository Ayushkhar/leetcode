# Last updated: 6/6/2026, 10:25:14 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head 
        cnt=1
        while curr.next!=None:
            cnt+=1
            curr=curr.next 
        a= cnt//2
        curr=head
        for i in range(a):
            curr=curr.next
        return curr 

            
      