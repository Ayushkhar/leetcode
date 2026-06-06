# Last updated: 6/6/2026, 10:27:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(-1)
        curr = dummynode
        carry = 0

        while l1 or l2:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0

            total = t1 + t2 + carry
            carry = total//10
            digit = total%10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        return dummynode.next
        