# Last updated: 6/6/2026, 10:25:37 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revlist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.revlist(l1)
        l2 = self.revlist(l2)
        dummy = ListNode(-1)
        curr= dummy
        carry = 0
        while l1 or l2 or carry:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0

            
            total = t1 + t2 + carry
            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)
            curr = curr.next


            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return self.revlist(dummy.next)


